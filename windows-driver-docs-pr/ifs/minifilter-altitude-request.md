---
title: Request a filter altitude identifier
description: Describes how to request a file system filter altitude, report a fractional altitude, or update information associated with an identifier
ms.date: 05/27/2021
keywords:
- filter altitude request
- minifilter altitude request
- WDK request a filter altitude
- WDK request a minifilter altitude
ms.localizationpriority: medium
---

# Request a filter altitude identifier

> [!NOTE]
> Microsoft will issue one "integer" altitude for each product type (by load order group). A company that already has a Microsoft-issued altitude can [create its own new altitude](load-order-groups-and-altitudes-for-minifilter-drivers.md#create-an-altitude) based on its Microsoft-assigned altitude to place a new filter in the same load order group.
>
> Microsoft will consider issuing multiple integer altitudes in the same load order group on a case-by-case basis.
>
> Previously issued altitudes will not change.

To request a [filter altitude identifier](load-order-groups-and-altitudes-for-minifilter-drivers.md), send email in an ASCII text e-mail message to [fsfcomm@microsoft.com](mailto:fsfcomm@microsoft.com?subject=Filter%20altitude%20request) with the subject: “Filter altitude request”, and the following fields and corresponding information:

| Field | Comment |
| ----- | ------- |
| Company name:    |  |
| Contact e-mail:  | Provide a long-term company email alias, versus individual email. The allocated filter altitude will be e-mailed back to this address. |
| Product name:    | Name of your filter product |
| Product URL:     | URL to your product or product's company |
| Product/Filter description: | A one paragraph summary to help Microsoft determine an appropriate altitude for the filter. |
| Filter filename: | Filename used for the filter |
| Filter type:     | One of these values: Registry, FileSystem, Both |
| Filter start-type: | One of these values: Boot, System, Auto, Demand |
| Requested filter load order group: | See [Load order groups and altitudes](load-order-groups-and-altitudes-for-minifilter-drivers.md) for the list of available groups. |
| Requested altitude: | You must request an altitude allocation in the appropriate [load order group or groups](load-order-groups-and-altitudes-for-minifilter-drivers.md) for your filter. Microsoft reserves the right to assign an altitude that is different from the requested altitude, depending on altitude availability and the filter driver functionality. |
| Additional information: | Use this field to let us know if there is any information you would like Microsoft to consider when assigning an altitude to this filter. |

## Example email for an altitude request

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

> [!NOTE]
>
> * All fields must be filled out.
>
> * It may take Microsoft up to two weeks to process and assign altitudes. Any missing information may delay the assignment.
>
> * The assigned altitude will eventually be listed in the [Allocated filter altitudes](allocated-altitudes.md) table.
