<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:f="http://hl7.org/fhir" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" exclude-result-prefixes="xsl xs fn f">
<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>

<xsl:variable name="var1" select="'Practitioner'" ></xsl:variable>

<xsl:variable name="basenodes">
<item>id</item>
<item>meta</item>
<item>implicitRules</item>
<item>language</item>
<item>text</item>
<item>contained</item>
</xsl:variable>

<!--======enter string in parent to search on here name here ==============--> 


	
	   <!-- Identity transform -->
 <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>

    </xsl:copy>
  </xsl:template>
  
  
  
  
 <!--=========remove the unwanted node from the snapshot to make a new diff===========--> 


 <!-- get rid of the resource and domain resource inherited elements -->

<xsl:template match="f:element[true() = (for $var2 in $basenodes/* return if(@id = concat($var1, '.' , $var2)) then true() else false())]">
</xsl:template>

<!--get rid of extension element they live in the extensions-->
<xsl:template match="f:element[matches(@id,'extension:.*?\.') or matches(@id,'modifierExtension:.*?\.') or ends-with(@id,'.id')  or ends-with(@id,'.url')]">
</xsl:template>


<!--get rid of naked extension elements-->

<xsl:template match="f:element[ends-with(@id,'.extension') and following-sibling::*[1][not(contains(@id,'extension'))]]">
</xsl:template>

<xsl:template match="f:element[ends-with(@id,'.modifierExtension') and following-sibling::*[1][not(contains(@id,'modifierExtension'))]]">
</xsl:template>


<!-- add must supports everywhere except on root and root extensions and ...-->
   <xsl:template match="f:isModifier[not(matches(../@id,$var1)) or not(ends-with(../@id,'.modifierExtension')) or not(ends-with../(@id,'.extension'))]"> 
 <mustSupport xmlns="http://hl7.org/fhir" value="true"/>
 <xsl:copy-of select="."/>
    </xsl:template>
    
    
   <!-- forgets the last item --> 
   <xsl:template match="f:isModifier[parent::*[last()]]"> 
 <mustSupport xmlns="http://hl7.org/fhir" value="true"/>
 <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="f:snapshot"><!-- change the snapshot to diff-->
   <differential xmlns="http://hl7.org/fhir"><xsl:apply-templates select="@*|node()" /></differential>
   </xsl:template>

  
  
  
</xsl:stylesheet>

