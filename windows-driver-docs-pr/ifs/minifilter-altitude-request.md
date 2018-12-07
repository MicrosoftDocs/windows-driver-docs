---
title: Minifilter Altitude Request
description: Minifilter Altitude Request
ms.assetid: 4861E5FC-9883-455F-A925-EBAFC890F568
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minifilter Altitude Request


A request for an minifilter altitude assignment is sent to Microsoft as an email. The body of the email must contain the following fields and corresponding information.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Company name:</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">Contact e-mail:</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">Product name:</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">Product URL:</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">Product/Filter description:</td>
<td align="left">A one paragraph summary to help Microsoft determine an appropriate altitude for the filter.</td>
</tr>
<tr class="even">
<td align="left">Filter filename:</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">Filter type:</td>
<td align="left">One of these values: Registry, FileSystem, Both</td>
</tr>
<tr class="even">
<td align="left">Filter start-type:</td>
<td align="left">One of these values: Boot, System, Auto, Demand</td>
</tr>
<tr class="odd">
<td align="left">Requested filter load order group:</td>
<td align="left">See the <a href="allocated-altitudes.md" data-raw-source="[File System Minifilter Allocated Altitudes](allocated-altitudes.md)">File System Minifilter Allocated Altitudes</a> for available load order groups.</td>
</tr>
<tr class="even">
<td align="left">Requested altitude:</td>
<td align="left">Microsoft reserves the right to assign an altitude that is different from the requested altitude, depending on altitude availability and the filter driver functionality.</td>
</tr>
<tr class="odd">
<td align="left">Additional information:</td>
<td align="left">Use this field to let us know if there is any information you would like Microsoft to consider when assigning an altitude to this filter.</td>
</tr>
</tbody>
</table>

 

Send this information in an ASCII text e-mail message to [fsfcomm@microsoft.com](mailto:fsfcomm@microsoft.com?subject=Minifilter%20altitude%20request) with the subject: “Minifilter altitude request”. An altitude for this filter will then be e-mailed back to the specified contact e-mail address.

The following is an example for the body of an allocation request email.

``` syntax
Hi,

Below is the request information to assign an altitude for our Contoso DataKleen file system minifilter.

Company name: Contoso Ltd.
Contact e-mail: filterdev@contoso.com
Product name: Contoso DataKleen
Product URL: http://fsfilters.contoso.com
Product/Filter Description:
    The Contoso DataKleen filter removes all occurences of any byte having a value
    between 128 and 255 during file reads. Our minifilter removes this value since
    it is not displayable on TTY devices.
Filter filename: ContosoDK.sys
Filter type: FileSystem
Filter start-type: Demand
Requested filter load order group: FSFilter Content Screener
Requested altitude: 268400
Additional information: None

Thanks,

FilterDev
```

**Note**  
-   All fields must be filled out.
-   It may take Microsoft up to two weeks to process and assign altitudes. Any missing information may delay the assignment.
-   The assigned altitude will eventually be reflected in the altitudes listed in [File System Minifilter Allocated Altitudes](allocated-altitudes.md). Please be aware that Microsoft only updates this list annually.

 

 

 




