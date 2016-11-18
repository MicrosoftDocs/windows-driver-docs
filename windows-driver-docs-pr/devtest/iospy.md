---
title: IoSpy
description: IoSpy
ms.assetid: 5fe52fe6-97b4-477a-9450-727c5bf9bd72
---

# IoSpy


IoSpy is a filter driver that records data about IOCTL and WMI requests made to the kernel-mode driver of a device.

You can install and remove IoSpy using the [Penetration Tests (Device Fundamentals)](coverage-tests--device-fundamentals-.md) tests, **Enable I/O Spy** and **Disable I/O Spy**. The *DQ* parameter controls which devices the IoSpy filter driver is installed on. IoSpy records the details about the IOCTL and WMI requests within the [IoSpy Data File](#iospy-data-file), which is used by [IoAttack](ioattack.md) to perform the fuzz tests.

**Important**  Before you run IoAttack, you must have previously run IoSpy and then removed it from the test system. For more information, see [How to Perform Fuzz tests with IoSpy and IoAttack](how-to-perform-fuzz-tests-with-iospy-and-ioattack.md).

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Disable_I_O_Spy"></span><span id="disable_i_o_spy"></span><span id="DISABLE_I_O_SPY"></span>Disable I/O Spy</p></td>
<td align="left"><p>Disable I/O Spy on 1 or more devices. Uninstalls IoSpy and disables IOCTL and WMI filtering for all devices on the test system.</p>
<p><strong>Test binary:</strong> Devfund_IOSpy_DisableSupport.wsc</p>
<p><strong>Test method:</strong> DisableIoSpy</p>
<p><strong>Parameters:</strong> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
<p><em>DQ</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Display_I_O_Spy-enabled_Device"></span><span id="display_i_o_spy-enabled_device"></span><span id="DISPLAY_I_O_SPY-ENABLED_DEVICE"></span>Display I/O Spy-enabled Device</p></td>
<td align="left"><p>Display devices that have I/O Spy enabled on them.</p>
<p><strong>Test binary:</strong> Devfund_IOSpy_DisplayEnabledDevices.wsc</p>
<p><strong>Test method:</strong> DisplayIoSpyDevices</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Enable_I_O_Spy_"></span><span id="enable_i_o_spy_"></span><span id="ENABLE_I_O_SPY_"></span>Enable I/O Spy</p></td>
<td align="left"><p>Installs IoSpy on the test system and enables IOCTL and WMI filtering on one or more devices. The DQ parameter controls which devices the IoSpy filter driver will get installed on.</p>
<p><strong>Test binary:</strong> Devfund_IOSpy_EnableSupport.wsc</p>
<p><strong>Test method:</strong> EnableIoSpy</p>
<p><strong>Parameters:</strong> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
<p><em>DQ</em></p>
<p><em>DFD</em> - specifies the path to the IoSpy data file. The default location is %SystemDrive%\DriverTest\IoSpy</p></td>
</tr>
</tbody>
</table>

 

### <span id="IoSpy_data_file"></span><span id="iospy_data_file"></span><span id="IOSPY_DATA_FILE"></span>IoSpy data file

After IoSpy is installed in a test system, it records the data sent through IOCTL and WMI requests to the drivers for devices enabled for fuzz tests. While IoSpy does not analyze the payloads of these requests, it does record the details of the requests such as the length of the payload buffers.

The *DFD* parameter for the **Enable I/O Spy** test specifies the path to the IoSpy data file. The default location is %SystemDrive%\\DriverTest\\IoSpy

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20IoSpy%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




