An extension to describe a health insurance product. A product is a discrete package of health insurance coverage benefits that are offered using a particular 
product network type (such as health maintenance organization, preferred provider organization, exclusive provider organization, point of service, or indemnity) within a service area.

This extension consists of a two-tier structure. The first tier describes a general category of coverage (e.g. medical, dental, mental health), while the second tier describes specific benefits associated with that coverage (e.g. hospitalization, primary care office visits):

*  `productCoverage.coverageType` - indicates a general category of coverage
*  `productCoverage.benefits.type` - indicates a specific type of benefit
*  `productCoverage.benefits.benefitList.description` - provides additional information about the benefit (e.g. indicates a unit, such as "number of days" or "visits," associated with the benefit)
*  `productCoverage.benefits.benefitList.value` - provides a specific value for the benefit

For example, the following attributes describe a product that includes a covered benefit of up to 60 visits per year by a home health aid:

coverageType = home health

benefits.type = home health aid

benefitList.description = visits per year

benefitList.value = 60

