---
title: Minifilter Altitude Request
description: Minifilter Altitude Request
ms.assetid: 4861E5FC-9883-455F-A925-EBAFC890F568
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minifilter Altitude Request

A file system minifilter driver developed to the Filter Manager model must have a unique identifier called an altitude that defines its position relative to other minifilters present in the file system stack.

To request a minifilter altitude identifier, send email in an ASCII text e-mail message to [fsfcomm@microsoft.com](mailto:fsfcomm@microsoft.com?subject=Minifilter%20altitude%20request) with the subject: “Minifilter altitude request”. The body of the email must contain the below fields and corresponding information.

An altitude for this filter will then be e-mailed back to the specified contact e-mail address.

You can also send email to [fsfcomm@microsoft.com](mailto:fsfcomm@microsoft.com?subject=Minifilter%20altitude%20request) to update information associated with existing altitudes.

|Field|Comment|
|----|----|
|Company name:| |
|Contact e-mail:|Provide a long-term company email alias, versus individual email.|
|Product name:| |
|Product URL:| |
|Product/Filter description:|A one paragraph summary to help Microsoft determine an appropriate altitude for the filter.|
|Filter filename:| |
|Filter type:|One of these values: Registry, FileSystem, Both|
|Filter start-type:|One of these values: Boot, System, Auto, Demand|
|Requested filter load order group:|See the [File System Minifilter Allocated Altitudes](allocated-altitudes.md) for available load order groups.|
|Requested altitude:|Microsoft reserves the right to assign an altitude that is different from the requested altitude, depending on altitude availability and the filter driver functionality.|
|Additional information:|Use this field to let us know if there is any information you would like Microsoft to consider when assigning an altitude to this filter.|

The following is an example for the body of an allocation request email.

``` syntax
Hi,

Below is the request information to assign an altitude for our Contoso DataKleen file system minifilter.

Company name: Contoso Ltd.
Contact e-mail: filterdevgroup@contoso.com
Product name: Contoso DataKleen
Product URL: http://fsfilters.contoso.com
Product/Filter Description: The Contoso DataKleen filter removes all occurrences of any byte having a value between 128 and 255 during file reads. Our minifilter removes this value since it is not displayable on TTY devices.
Filter filename: ContosoDK.sys
Filter type: FileSystem
Filter start-type: Demand
Requested filter load order group: FSFilter Content Screener
Requested altitude: 268400
Additional information: None

Thanks,

FilterDev
```

>[!NOTE]
>- All fields must be filled out.
>- It may take Microsoft up to two weeks to process and assign altitudes. Any missing information may delay the assignment.
>- The assigned altitude will eventually be reflected in the altitudes listed in [File System Minifilter Allocated Altitudes](allocated-altitudes.md). Please be aware that Microsoft only updates this list annually.
