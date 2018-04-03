# Get all products

Use this method in the Microsoft Hardware API to retrieve data for all
the products registered to your Windows Dev Center account.

[]{#_Toc510098049 .anchor}Prerequisites

If you have not done so already, complete all the
[[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
Hardware APIs before trying to use any of these methods.

[]{#_Toc510098050 .anchor}Request

This method has the following syntax. See the following sections for
usage examples and descriptions of the header and request body.

  Method   Request URI
  -------- -----------------------------------------------------------------------
  GET      https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/

[]{#_Toc510098051 .anchor}Request header

  Header          Type     Description
  --------------- -------- ------------------------------------------------------------------------------
  Authorization   string   Required. The Azure AD access token in the form **Bearer** *\<token\>*.
  accept          string   Optional. Specifies the type of content. Allowed value is "application/json"

[]{#_Toc510098052 .anchor}Request parameters

Do not provide request parameters for this method.

[]{#_Toc510098053 .anchor}Request body

Do not provide a request body for this method.

[]{#_Toc510098054 .anchor}Request examples

The following example demonstrates how to retrieve information about all
products that are registered to your account.

Copy

GET
https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/
HTTP/1.1

Authorization: Bearer \<your access token\>

[]{#_Toc510098055 .anchor}Response

The following example demonstrates the JSON response body returned by a
successful request for all the products that are registered to a
developer account. For brevity, this example only shows the data for the
first two products returned by the request. For more details about the
values in the response body, see the following section.

JSON Copy

{

\"value\": \[

{

\"id\": 9007199267351834,

\"sharedProductId\": 1152921504606971100,

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351834\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351834/submissions\",

\"rel\": \"get\_submissions\",

\"method\": \"GET\"

}

\],

\"isCommitted\": true,

\"isExtensionInf\": false,

\"deviceMetadataIds\": \[\],

\"deviceType\": \"notSet\",

\"isTestSign\": false,

\"marketingNames\": \[\],

\"productName\": \"NewDriverHacked\",

\"selectedProductTypes\": {},

\"requestedSignatures\": \[

\"WINDOWS\_v100\_X64\_TH1\_FULL\",

\"WINDOWS\_v63\_X64\"

\],

\"additionalAttributes\": {},

\"testHarness\": \"hlk\"

},

{

\"id\": 9007199267351836,

\"sharedProductId\": 1152921504606971100,

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351835\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351835/submissions\",

\"rel\": \"get\_submissions\",

\"method\": \"GET\"

}

\],

\"isCommitted\": true,

\"isExtensionInf\": false,

\"announcementDate\": \"2016-10-22T00:00:00Z\",

\"deviceMetadataCategory\": \"Input.Digitizer.Multitouch\",

\"deviceMetadataIds\": \[\],

\"deviceType\": \"internalExternal\",

\"isTestSign\": false,

\"marketingNames\": \[

\"MEU\"

\],

\"productName\": \"Mew2?\",

\"selectedProductTypes\": {

\"windows\_v100\": \"Touch\",

\"windows81\": \"Unclassified\"

},

\"requestedSignatures\": \[

\"WINDOWS\_v100\_X64\_TH1\_FULL\",

\"WINDOWS\_v63\_X64\"

\],

\"additionalAttributes\": {},

\"testHarness\": \"hlk\"

}

\],

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products?pageSize=50\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products?pageSize=50&continuationToken=PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTE2Ij8%2BPENvbnRpbnVhdGlvblRva2VuPjxWZXJzaW9uPjIuMDwvVmVyc2lvbj48VHlwZT5UYWJsZTwvVHlwZT48TmV4dFBhcnRpdGlvbktleT4xITQ4IWNIVmliR2x6YUdWeWN5MHdNREF3TURBd01EQXdNREF3TURBd01ESTVPVFl6T1RJdzwvTmV4dFBhcnRpdGlvbktleT48TmV4dFJvd0tleT4xITk2IWRYTmxjaTFrWld4bGRHVmtMVEF0SUNBZ0lDQWdTR0Z5WkhkaGNtVkVjbWwyWlhJdGNISnZaSFZqZEhNdE1EQXdNREF3TURBd09UQXdOekU1T1RJMk56TTNNakUyTkEtLTwvTmV4dFJvd0tleT48VGFyZ2V0TG9jYXRpb24%2BUHJpbWFyeTwvVGFyZ2V0TG9jYXRpb24%2BPC9Db250aW51YXRpb25Ub2tlbj4%3D\",

\"rel\": \"next\_link\",

\"method\": \"GET\"

}

\]

}

[]{#_Toc510098056 .anchor}Response body

  Value   Type    Description
  ------- ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  value   array   An array of objects that contain information about each product that is registered to your account. For more information about the data in each object, see [Product resource](#ProductResource).
  links   array   An array of objects with helpful links about the containing entity. Refer [link object](#LinkResource) for more details

[]{#_Toc510098057 .anchor}Error codes

Refer [error codes](#ErrorCodes) for details.