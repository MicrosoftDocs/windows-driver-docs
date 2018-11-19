---
title: Registering Hardware Information
description: Registering Hardware Information
ms.assetid: 1fec9fcf-3ec7-4926-9ceb-ef1f7f42e963
keywords:
- registry WDK display
- hardware information in registry WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Hardware Information


To display useful information to the user and for assistance in debugging, a display miniport driver must set certain hardware information in the registry. A display miniport driver must set a chip type, digital-to-analog converter (DAC) type, memory size (of the adapter), and a string to identify the adapter. This information is shown by the **Display** application in Control Panel. Typically, the driver sets this information in its [**DxgkDdiAddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff559586) function.

To set this information, the driver:

1.  Calls the [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443) function to open and obtain a handle to a [*software key*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key) for storing driver-specific information. In this call, the driver specifies the PLUGPLAY\_REGKEY\_DRIVER flag in the *DevInstKeyType* parameter and the KEY\_SET\_VALUE, KEY\_WRITE, or KEY\_ALL\_ACCESS value in the *DesiredAccess* parameter.

2.  Calls the [**ZwSetValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567109) function several times to set each type of hardware information. In each call, the driver specifies, in the *KeyHandle* parameter, the software-key handle that was obtained from **IoOpenDeviceRegistryKey**.

    The following table describes the information that the driver must register and provides details for the *ValueName* and *Data* parameters of **ZwSetValueKey**:

    <table>
    <colgroup>
    <col width="33%" />
    <col width="33%" />
    <col width="33%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Information for entry</th>
    <th align="left"><em>ValueName</em> parameter</th>
    <th align="left"><em>Data</em> parameter</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>Chip type</p></td>
    <td align="left"><p>HardwareInformation.ChipType</p></td>
    <td align="left"><p>Null-terminated string that contains the chip name</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>DAC type</p></td>
    <td align="left"><p>HardwareInformation.DacType</p></td>
    <td align="left"><p>Null-terminated string that contains the DAC name or identifier (ID)</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Memory size</p></td>
    <td align="left"><p>HardwareInformation.MemorySize</p></td>
    <td align="left"><p>ULONG that contains, in megabytes, the amount of video memory on the adapter</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Adapter ID</p></td>
    <td align="left"><p>HardwareInformation.AdapterString</p></td>
    <td align="left"><p>Null-terminated string that contains the name of the adapter</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>BIOS</p></td>
    <td align="left"><p>HardwareInformation.BiosString</p></td>
    <td align="left"><p>Null-terminated string that contains information about the BIOS</p></td>
    </tr>
    </tbody>
    </table>

     

 

 





