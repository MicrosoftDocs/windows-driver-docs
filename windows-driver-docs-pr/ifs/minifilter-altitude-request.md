---
title: Minifilter Altitude Request
author: windows-driver-content
description: Minifilter Altitude Request
ms.assetid: 4861E5FC-9883-455F-A925-EBAFC890F568
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
<td align="left">See the [File System Minifilter Allocated Altitudes](allocated-altitudes.md) for available load order groups.</td>
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Minifilter%20Altitude%20Request%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


