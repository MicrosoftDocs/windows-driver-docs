---
title: USB Device-Specific Method (\_DSM)
author: windows-driver-content
description: To support device-class-specific configuration of the USB subsystem, Windows defines a Device-Specific Method (\_DSM) that has the functions that are described in this article.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8F0EDE17-9895-4C24-B061-963DA0D7882B
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

**Note**  Function index 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For more information, see section 9.14.1, "\_DSM (Device Specific Method)", in the [ACPI 5.0 specification](http://www.acpi.info).

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20USB%20Device-Specific%20Method%20%28_DSM%29%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


