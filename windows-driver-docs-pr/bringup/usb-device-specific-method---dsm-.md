---
title: USB Device-Specific Method (_DSM)
description: To support device-class-specific configuration of the USB subsystem, Windows defines a Device-Specific Method (_DSM) that has the functions that are described in this article.
ms.assetid: 8F0EDE17-9895-4C24-B061-963DA0D7882B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Device-Specific Method (\_DSM)


To support device-class-specific configuration of the USB subsystem, Windows defines a Device-Specific Method (\_DSM) that has the functions that are described in this article.

## Function 1: Post-reset processing for dual-role controllers


The \_DSM control method parameters for the post-reset processing function for dual-role USB controllers are as follows:

### Arguments

-   **Arg0:** UUID = ce2ee385-00e6-48cb-9f05-2edb927c4899
-   **Arg1:** Revision ID = 0
-   **Arg2:** Function index = 1
-   **Arg3:** Empty package (not used)

### Return

None
The Windows inbox drivers only support USB controllers in host mode. After each controller reset, the USB driver will invoke the \_DSM function index 1 to perform any controller-specific initialization required to configure the USB controller to operate in host mode.

When this function is used, the \_DSM method must appear under the USB controller device.

## Function 2: Port type identification


The \_DSM control method parameters for identifying the USB port type are as follows:

### Arguments

-   **Arg0:** UUID = ce2ee385-00e6-48cb-9f05-2edb927c4899
-   **Arg1:** Revision ID = 0
-   **Arg2:** Function index = 2
-   **Arg3:** Empty package (not used)

### Return

An integer containing one of the following values:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Object type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Port type</td>
<td>Integer (BYTE)</td>
<td><p>Specifies the type of the USB port:</p>
<ul>
<li>0x00 – Regular USB</li>
<li>0x01 – HSIC</li>
<li>0x02 – SSIC</li>
<li>0x03 – 0xff reserved</li>
</ul></td>
</tr>
</tbody>
</table>

 

When this function is used, the \_DSM method must appear under the USB port device.

**Note**  Function index 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For more information, see section 9.14.1, "\_DSM (Device Specific Method)", in the [ACPI 5.0 specification](https://www.uefi.org/specifications).

 

 

 




