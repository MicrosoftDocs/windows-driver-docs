---
title: Registering Hardware Information
description: Registering Hardware Information
ms.assetid: 1fec9fcf-3ec7-4926-9ceb-ef1f7f42e963
keywords:
- registry WDK display
- hardware information in registry WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

     

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Registering%20Hardware%20Information%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




