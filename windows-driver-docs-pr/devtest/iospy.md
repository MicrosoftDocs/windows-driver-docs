---
title: IoSpy
description: IoSpy is a filter driver that records data about IOCTL and WMI requests made to the kernel-mode driver of a device.
ms.assetid: 5fe52fe6-97b4-477a-9450-727c5bf9bd72
ms.date: 07/09/2018
ms.localizationpriority: medium
---

> [!NOTE]
> IoSpy and IoAttack are no longer available in the WDK after Windows 10 Version 1703.
>
> As an alternative to these tools, consider using the fuzzing tests available in the HLK. Here are a few to consider.
> 
> [DF - Fuzz random IOCTL test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/236b8ad5-0ba1-4075-80a6-ae9dafb71c94)
>
> [DF - Fuzz sub-opens test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/92bf534e-aa48-4aeb-b3cd-e46fb7cc7d80)
>
> [DF - Fuzz zero length buffer FSCTL test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/5f5f6c7e-d5db-4ff1-8cee-da47203ab070)
>
> [DF - Fuzz random FSCTL test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/e529e34e-076a-4978-926f-7eca333e8f4d)
>
> [DF - Fuzz Misc API test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/fb305d04-6e8c-4dfc-9984-9692df82fbd8)
>
> You can also use the [Kernel synchronization delay fuzzing](https://docs.microsoft.com/windows-hardware/drivers/devtest/kernel-synchronization-delay-fuzzing) that is included with Driver Verifier.
>



# IoSpy


IoSpy is a filter driver that records data about IOCTL and WMI requests made to the kernel-mode driver of a device.

You can install and remove IoSpy using the [Penetration Tests (Device Fundamentals)](coverage-tests--device-fundamentals-.md) tests, **Enable I/O Spy** and **Disable I/O Spy**. The *DQ* parameter controls which devices the IoSpy filter driver is installed on. IoSpy records the details about the IOCTL and WMI requests within the [IoSpy data file](#iospy-data-file), which is used by [IoAttack](ioattack.md) to perform the fuzz tests.

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
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
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
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>DFD</em> - specifies the path to the IoSpy data file. The default location is %SystemDrive%\DriverTest\IoSpy</p></td>
</tr>
</tbody>
</table>

 

## IoSpy data file

After IoSpy is installed in a test system, it records the data sent through IOCTL and WMI requests to the drivers for devices enabled for fuzz tests. While IoSpy does not analyze the payloads of these requests, it does record the details of the requests such as the length of the payload buffers.

The *DFD* parameter for the **Enable I/O Spy** test specifies the path to the IoSpy data file. The default location is %SystemDrive%\\DriverTest\\IoSpy

 

 





