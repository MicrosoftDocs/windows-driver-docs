---
title: INF Requirements for Hyper-V Extensible Switch Extensions
description: INF Requirements for Hyper-V Extensible Switch Extensions
ms.assetid: 378F619A-C799-4330-A388-9955A67251F8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Requirements for Hyper-V Extensible Switch Extensions


Hyper-V extensible switch extensions are developed as NDIS filter drivers. As a result, the INF requirements for extensions are based on the INF requirements for all NDIS filter drivers. When you create an INF file for an extensible switch extension, you should use the INF settings for a modifying or monitoring filter driver. For more information on these settings, see [INF File Settings for Filter Drivers](inf-file-settings-for-filter-drivers.md).

In addition, you must follow these guidelines for INF files for extensible switch extensions:

- An extensible switch extension must be installed as a modifying filter driver.

  For more information on the INF requirements for a modifying filter driver, see [Configuring an INF File for a Modifying Filter Driver](configuring-an-inf-file-for-a-modifying-filter-driver.md).

  **Note**  An extension with a filter class of **ms\_switch\_capture** can perform the same tasks as a monitoring filter driver. For more information, see [Types of Filter Drivers](types-of-filter-drivers.md).

     

- The **FilterMediaTypes** entry in the filter INF file defines the driver's bindings to other drivers and interfaces. The **FilterMediaTypes** entry for an extensible switch extension must include the **vmnetextension** value. This value specifies a binding to the extensible switch extension miniport adapter.

  The **FilterMediaTypes** entry allows a comma-delimited list of media types to be specified. This allows the extension to be bound to a physical interface or to the extensible switch interface.

  The following example shows a **FilterMediaTypes** entry that allows an extension to be bound to either the physical Ethernet network adapter or an extensible switch virtual network adapter.

  ```INF
  HKR, Ndi\Interfaces, FilterMediaTypes, , "ethernet, vmnetextension"
  ```

  If the **FilterMediaTypes** entry only specifies the **vmnetextension** value, the extension will only bind to the driver stacks for all extensible switches on the system.

  If the **FilterMediaTypes** entry specifies **vmnetextension** as well as other media types, the extension can determine whether it is bound within an extensible switch driver stack by calling [**NdisFGetOptionalSwitchHandlers**](https://msdn.microsoft.com/library/windows/hardware/hh598204). If the function returns NDIS\_STATUS\_SUCCESS, the extension is bound within the extension driver stack. If the function returns NDIS\_STATUS\_NOT\_SUPPORTED, the extension is bound within the driver stack for a different physical network interface.

  For more information about the **FilterMediaTypes** entry, see [Intermediate Driver UpperRange And LowerRange INF File Entries](intermediate-driver-upperrange-and-lowerrange-inf-file-entries.md).

- The **FilterClass** value in the INF file for an extension determines its order in a stack of filters. The **FilterClass** entry must contain one of the values from the following table.

  <table>
  <colgroup>
  <col width="50%" />
  <col width="50%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th align="left">FilterClass value</th>
  <th align="left">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td align="left"><p><strong>ms_switch_capture</strong></p></td>
  <td align="left"><p>An extension of this class monitors packet traffic. However, this class of extension cannot apply port policies or alter destination ports for a packet.</p>
  <p>For more information about this class of extension, see <a href="capturing-extensions.md" data-raw-source="[Capturing Extensions](capturing-extensions.md)">Capturing Extensions</a>.</p></td>
  </tr>
  <tr class="even">
  <td align="left"><p><strong>ms_switch_filter</strong></p></td>
  <td align="left"><p>An extension of this class filters packet traffic and enforces port or switch policy for packet delivery through the extensible switch. This class of driver can also inspect and remove destination ports for each packet based on policy settings.</p>
  <p>For more information about this class of extension, see <a href="filtering-extensions.md" data-raw-source="[Filtering Extensions](filtering-extensions.md)">Filtering Extensions</a>.</p></td>
  </tr>
  <tr class="odd">
  <td align="left"><p><strong>ms_switch_forward</strong></p></td>
  <td align="left"><p>An extension of this class has the same capabilities as the <strong>ms_switch_filter</strong> class. This class of extension can also forward packets to other extensible switch ports, as well as inject packet traffic to any extensible switch port.</p>
  <p>On the ingress data path, this class of extension is invoked after the <strong>ms_switch_filter</strong> class of extension. On the egress data path, this class of extension is invoked before the <strong>ms_switch_filter</strong> class of extension.</p>
  <p>For more information about this class of extension, see <a href="forwarding-extensions.md" data-raw-source="[Forwarding Extensions](forwarding-extensions.md)">Forwarding Extensions</a>.</p>
  <div class="alert">
  <strong>Note</strong>  Only one extension of this class is allowed in the extensible switch driver stack.
  </div>
  <div>
     
  </div></td>
  </tr>
  </tbody>
  </table>

     

When the extension is installed with these INF settings, it will be configured to bind to every extensible switch instance. However, the binding will be disabled and must be explicitly enabled through a PowerShell cmdlet. For more information on this procedure, see [Enabling Hyper-V Extensible Switch Extensions](enabling-hyper-v-extensibility-switch-extensions.md).

 

 





