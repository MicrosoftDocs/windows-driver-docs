---
title: PnP Tests (Device Fundamentals)
description: The Device Fundamentals PnP tests force a driver to handle almost all of the PnP IRPs; however, there are three areas that are stressed specifically removal, rebalance, and surprise removal.
ms.assetid: 4224F92B-5430-4F55-900D-0B08ADBE54F6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PnP Tests (Device Fundamentals)


The Device Fundamentals PnP tests force a driver to handle almost all of the PnP IRPs; however, there are three areas that are stressed specifically: removal, rebalance, and surprise removal. The PnP test provides a mechanism to test each of these separately, or to test them all together (that is, as a stress test). This PnP testing is accomplished by using a combination of user-mode API calls (through the test application) and kernel-mode API calls (through an upper-filter driver).

## PNP tests


The Plug and Play (PnP) tests execute various PnP-related code paths in the driver and user-mode components. The PnP tests should be run with [Driver Verifier](driver-verifier.md) enabled on the test computer. For information about enabling Driver Verifier, see [Driver Verifier properties for driver projects](https://msdn.microsoft.com/windows-drivers/develop/driver_verifier_properties_for__driver_projects).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Test</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Disable_Enhanced_Device_Testing__EDT__Support_"></span><span id="disable_enhanced_device_testing__edt__support_"></span><span id="DISABLE_ENHANCED_DEVICE_TESTING__EDT__SUPPORT_"></span>Disable Enhanced Device Testing (EDT) Support</p></td>
<td align="left"><p>This test uninstalls the test filter driver (msdmfilt.sys) as an upper filter on devices specified using the DQ parameter. This test filter gets installed as part of running tests in this test category</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p>
<p><em>IOType</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="PNP__disable_and_enable__reboot_with_IO_before_and_after"></span><span id="pnp__disable_and_enable__reboot_with_io_before_and_after"></span><span id="PNP__DISABLE_AND_ENABLE__REBOOT_WITH_IO_BEFORE_AND_AFTER"></span>PNP (disable and enable) reboot with IO before and after</p></td>
<td align="left"><p>This test performs basic PnP disable/enable and I/O on devices with a system reboot.</p>
<p><strong>Test binary:</strong> Devfund_PNP_DisableEnable_Reboot_With_IO_BeforeAndAfter.wsc</p>
<p><strong>Test method:</strong> PNP_DisableEnable_Reboot_With_IO_Before_And_After</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="PNP__disable_and_enable__with_I_O_before_and_after"></span><span id="pnp__disable_and_enable__with_i_o_before_and_after"></span><span id="PNP__DISABLE_AND_ENABLE__WITH_I_O_BEFORE_AND_AFTER"></span>PNP (disable and enable) with I/O before and after</p></td>
<td align="left"><p>This test performs I/O and basic PnP disable/enable on devices.</p>
<p>This test does the following:</p>
<ol>
<li>Verifies that there are no devices on the system reporting device problem codes.</li>
<li>Tests I/O on every device on the system using WDTF Simple I/O plugins. See <a href="https://msdn.microsoft.com/library/windows/hardware/hh781398" data-raw-source="[Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398)">Provided WDTF Simple I/O plug-ins</a> for more information.</li>
<li>Disables and enables every device on the system using WDTF PnP action interfaces, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451068" data-raw-source="[&lt;strong&gt;IWDTFPNPAction2::DisableDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451068)"><strong>IWDTFPNPAction2::DisableDevice</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh451082" data-raw-source="[&lt;strong&gt;IWDTFPNPAction2::EnableDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451082)"><strong>IWDTFPNPAction2::EnableDevice</strong></a> methods for more information.</li>
<li>Verifies that there are no devices on the system reporting device problem codes.</li>
<li>Tests I/O on every device on the system using WDTF Simple I/O plugins. See <a href="https://msdn.microsoft.com/library/windows/hardware/hh781398" data-raw-source="[Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398)">Provided WDTF Simple I/O plug-ins</a> for more information.</li>
<li>Repeats steps 3-5 several times.</li>
</ol>
<p><strong>Test binary:</strong> Devfund_PNP_DisableEnable_With_IO_BeforeAndAfter.wsc</p>
<p><strong>Test method:</strong> PNP_DisableEnable_With_IO_Before_And_After</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="PNP_Cancel_Remove_Device_test_"></span><span id="pnp_cancel_remove_device_test_"></span><span id="PNP_CANCEL_REMOVE_DEVICE_TEST_"></span>PNP Cancel Remove Device test</p></td>
<td align="left"><p>This test uses the EDT filter driver to send IRP_MN_CANCEL_REMOVE_DEVICE to target device stacks.</p>
<p>For more information, see <a href="#about-the-device-removal-tests" data-raw-source="[About the Device Removal tests](#about-the-device-removal-tests)">About the Device Removal tests</a>.</p>
<p><strong>Test binary:</strong> Devfund_PnPDTest.dll</p>
<p><strong>Test method:</strong> PNPCancelRemoveDevice</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="PNP_Cancel_Stop_Device_test"></span><span id="pnp_cancel_stop_device_test"></span><span id="PNP_CANCEL_STOP_DEVICE_TEST"></span>PNP Cancel Stop Device test</p></td>
<td align="left"><p>This test uses the EDT filter driver to send IRP_MN_CANCEL_STOP_DEVICE to target device stacks.</p>
<p>For more information, see <a href="#about-the-rebalance-tests" data-raw-source="[About the Rebalance tests](#about-the-rebalance-tests)">About the Rebalance tests</a>.</p>
<p><strong>Test binary:</strong> Devfund_PnPDTest.dll</p>
<p><strong>Test method:</strong> PNPCancelStopDevice</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="PNP_DIF_Remove_Device_Test"></span><span id="pnp_dif_remove_device_test"></span><span id="PNP_DIF_REMOVE_DEVICE_TEST"></span>PNP DIF Remove Device Test</p></td>
<td align="left"><p>This test uses the SetupDi API to send a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543717" data-raw-source="[&lt;strong&gt;DIF_REMOVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543717)"><strong>DIF_REMOVE</strong></a> request for the installers to remove the device.</p>
<p><strong>Test binary:</strong> Devfund_PnPDTest.dll</p>
<p><strong>Test method:</strong> PNPDIFRemoveAndRescanParentDevice</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="PNP_Disable_and_Enable_Device_test_"></span><span id="pnp_disable_and_enable_device_test_"></span><span id="PNP_DISABLE_AND_ENABLE_DEVICE_TEST_"></span>PNP Disable and Enable Device test</p></td>
<td align="left"><p>This test disables and enables the target devices.</p>
<p><strong>Test binary:</strong> Devfund_PnPDTest.dll</p>
<p><strong>Test method:</strong> PNPDisableAndEnableDevice</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p>
<p><em>IOType</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="PNP_Rebalance_Fail_Restart_Device_test"></span><span id="pnp_rebalance_fail_restart_device_test"></span><span id="PNP_REBALANCE_FAIL_RESTART_DEVICE_TEST"></span>PNP Rebalance Fail Restart Device test</p></td>
<td align="left"><p>This test uses the EDT filter driver to try to send IRP_MN_STOP_DEVICE to target device stacks. The EDT filter driver then fails IRP_MN_START_DEVICE requests (that follow IRP_MN_STOP_DEVICE requests) to trigger the surprise removal of target devices.</p>
<p>For more information, see <a href="#about-the-rebalance-tests" data-raw-source="[About the Rebalance tests](#about-the-rebalance-tests)">About the Rebalance tests</a>.</p>
<p><strong>Test binary:</strong> Devfund_PnPDTest.dll</p>
<p><strong>Test method:</strong> PNPTryStopDeviceAndFailRestart</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="PNP_Rebalance_Request_New_Resources_Device_test"></span><span id="pnp_rebalance_request_new_resources_device_test"></span><span id="PNP_REBALANCE_REQUEST_NEW_RESOURCES_DEVICE_TEST"></span>PNP Rebalance Request New Resources Device test</p></td>
<td align="left"><p>This test uses the EDT filter driver to try to send IRP_MN_STOP_DEVICE to target device stacks. It also manipulates the resource requirements of the devices to maximize the chances that new resources are allocated to devices.</p>
<p>For more information, see <a href="#about-the-rebalance-tests" data-raw-source="[About the Rebalance tests](#about-the-rebalance-tests)">About the Rebalance tests</a>.</p>
<p><strong>Test binary:</strong> Devfund_PnPDTest.dll</p>
<p><strong>Test method:</strong> PNPTryStopDeviceRequestNewResourcesAndRestartDevice</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="PNP_Remove_Device_Test"></span><span id="pnp_remove_device_test"></span><span id="PNP_REMOVE_DEVICE_TEST"></span>PNP Remove Device Test</p></td>
<td align="left"><p>This test causes IRP_MN_QUERY_REMOVE_DEVICE and IRP_MN_REMOVE_DEVICE to be sent to target device stacks.</p>
<p>For more information, see <a href="#about-the-device-removal-tests" data-raw-source="[About the Device Removal tests](#about-the-device-removal-tests)">About the Device Removal tests</a>.</p>
<p><strong>Test binary:</strong> Devfund_PnPDTest.dll</p>
<p><strong>Test method:</strong> PNPRemoveAndRestartDevice</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="PNP_Stop__Rebalance__Device_test"></span><span id="pnp_stop__rebalance__device_test"></span><span id="PNP_STOP__REBALANCE__DEVICE_TEST"></span>PNP Stop (Rebalance) Device test</p></td>
<td align="left"><p>This test uses the EDT filter driver to try to send IRP_MN_STOP_DEVICE to target device stacks.</p>
<p>For more information, see <a href="#about-the-rebalance-tests" data-raw-source="[About the Rebalance tests](#about-the-rebalance-tests)">About the Rebalance tests</a>.</p>
<p><strong>Test binary:</strong> Devfund_PnPDTest.dll</p>
<p><strong>Test method:</strong> PNPTryStopAndRestartDevice</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="PNP_Surprise_Remove_Device_test"></span><span id="pnp_surprise_remove_device_test"></span><span id="PNP_SURPRISE_REMOVE_DEVICE_TEST"></span>PNP Surprise Remove Device test</p></td>
<td align="left"><p>This test uses the EDT filter driver to send IRP_MN_SURPRISE_REMOVAL to target device stacks.</p>
<p>For more information, see <a href="#about-the-surprise-removal-test" data-raw-source="[About the Surprise Removal test](#about-the-surprise-removal-test)">About the Surprise Removal test</a>.</p>
<p><strong>Test binary:</strong> Devfund_PnPDTest.dll</p>
<p><strong>Test method:</strong> PNPSurpriseRemoveAndRestartDevice</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>DoSimpleIO</em></p>
<p><em>IOPeriod</em></p>
<p><em>DoConcurrentIO</em></p></td>
</tr>
</tbody>
</table>

 

## About the Device Removal tests


- PNP Remove Device Test
- PNP Cancel Remove Device test

The Device Removal test encompasses IRP\_MN\_QUERY\_REMOVE\_DEVICE, IRP\_MN\_CANCEL\_REMOVE\_DEVICE, and IRP\_MN\_REMOVE\_DEVICE.

The test attempts to install its upper-filter driver on the target device stack. This attempt results in a query-remove IRP.

If this query-remove IRP fails, the test restarts the computer to get the filter driver onto the device stack. If the remove request is not vetoed, the device stack will be removed and restarted with the filter driver on the device stack.

The test, by using setup APIs, causes a query-remove IRP to be sent to the device stack. The filter driver fails this remove request, so a cancel-remove IRP is sent. The filter driver will assert that the cancel-remove was successful.

Next, the test application calls the appropriate class installer and any registered co-installers to disable or enable and remove or reenumerate the device (this tests the class and co-installers handling of DIF\_PROPERTYCHANGE with DICS\_DISABLE, DICS\_ENABLE, and DICS\_PROPCHANGE). When receiving IRP\_MN\_REMOVE\_DEVICE, the filter driver will assert that the lower drivers completed it successfully.

Each of these steps involves a preliminary remove request. If that request is vetoed, the device will not be removed. You can choose to veto a remove request when appropriate, such as while streaming video on a USB camera or if the target device is in the boot or paging path. Remember that simply failing all remove requests is generally not good practice. Failing all remove requests will not guarantee that driver will never receive a remove because a remove IRP will still be issued after a surprise removal, or if anyone in the device stack fails a start IRP.

## About the Surprise Removal test


- PNP Surprise Remove Device test

The Surprise Removal test encompasses IRP\_MN\_SURPRISE\_REMOVAL followed by IRP\_MN\_REMOVE\_DEVICE.

As with the previous tests, the test application will attempt to add an upper filter to the target device stack and then restart the stack. If this attempt is not successful, the test restarts the computer.

When triggered by the test application, the filter driver will cause the system to send an IRP\_MN\_SURPRISE\_REMOVAL to the device stack, followed by an IRP\_MN\_REMOVE\_DEVICE. The filter driver will assert that both of these IRPs are completed successfully by lower drivers.

After the surprise removal test is complete, the device will be uninstalled and reenumerated, also removing the filter driver from the stack.

## About the Rebalance Tests


- PNP Stop (Rebalance) Device test
- PNP Rebalance Request New Resources Device test
- PNP Rebalance Fail Restart Device test
- PNP Cancel Stop Device test

As with the removal test, the test application attempts to add an upper filter to the target device stack and then restart the device stack by using **SetupDiCallClassInstaller** with DIF\_PROPERTYCHANGE. If this attempt is not successful (that is, if someone on the target device stack failed the query-remove IRP), the test restarts the computer to test rebalance.

Depending upon which rebalance test that you choose, the following events occur:

1.  **PNP Stop (Rebalance) Device test** This test initiates a rebalance procedure which results in the IRP\_MN\_QUERY\_STOP\_DEVICE PnP IRP to the device driver.

    If any driver in the stack fails this IRP the rebalance procedure is abandoned. Please note that in Windows Vista, there is support for multi-level rebalance. If a rebalance is started on a non-leaf device node, all of the device stacks that are present in the device tree with that device node as the root also go through rebalance. And if any of the child device stacks fails query stop, the whole rebalance procedure is abandoned. So drivers must not fail query stop without a genuine reason to do so. If this failure happens, the PnP manager sends cancel stop (IRP\_MN\_CANCEL\_STOP) to all the device stacks that had been sent query stop.

    If all of the device stacks involved pass query stop, the test continues with the rebalance and sends the IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS and IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS IRPS to find the resource requirement of the devices.

    After this point, two different paths are possible depending on whether the target device consumes any resources or not:

    -   If the device does not consume any resources, the PnP manager itself sends a cancel stop (IRP\_MN\_CANCEL\_STOP\_DEVICE) as an optimization.

        If the device actually consumes resources, the rebalance procedure is completed with the IRP\_MN\_STOP\_DEVICE and IRP\_MN\_START\_DEVICE IRPs.

    With this option, the resources of the device do not change.

2.  **PNP Cancel Stop Device test**: This test initiates a rebalance procedure, but the filter driver deliberately fails the query stop IRP. The order of IRPs looks like IRP\_MN\_QUERY\_STOP\_DEVICE (which is failed by the filter driver while coming up, causing a cancellation of rebalance) and IRP\_MN\_CANCEL\_STOP\_DEVICE.

    With this option, the resources of the device do not change

3.  **PNP Rebalance Request New Resources Device test** This test initiates a rebalance and also manipulates the resource requirement of the device to maximize the chances that actually new resources are allocated to the device. This option also helps a device with no resources to actually go through the complete rebalance procedure:
    1.  First the simple rebalance is started, causing the following IRPs:
        -   IRP\_MN\_QUERY\_STOP\_DEVICE (assuming this IRP is passed by all the drivers. The test already covered the case where this IRP is failed.)
        -   IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS
        -   IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS. In response to this IRP, while going up, filter driver takes action based on whether the device consumes any resources or not:
            -   If the device has no resource requirement, filter assigns a fake resource.
            -   If the device has a resource requirement, it tries to restructure the resource requirement list in such a way that maximizes the probability of changing the current assignment. For example, if a device needs 2 bytes of memory anywhere between 00 to FF and currently is assigned 3A-3B, modify such that the new resource requirement (in order of preference) looks like 00-39 or 3C-FF or 3A-3B. Similarly if the device resource requirement list has any alternate requirements, it will change their order so the alternate requirement comes earlier in the list.

    2.  Now the device should always complete the rebalance procedure.

        IRP\_MN\_STOP\_DEVICE

        IRP\_MN\_START\_DEVICE (The new allocated resources. If fake requirements were created, mask the new resources from the actual drivers.)

4.  **PNP Rebalance Fail Restart Device Test** This test initiates a rebalance but when the filter driver gets the start after the rebalance, it deliberately fails it-which causes the surprise removal IRP followed by Removal IRP.

    First, it starts the rebalance procedure and makes sure that the driver gets a stop and a start by generating fake resource requirement for a device which does not consume any resources.

    -   IRP\_MN\_QUERY\_STOP\_DEVICE (assuming this IRP is passed by all the drivers. The test already covered the case where this IRP is failed.)
    -   IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS
    -   IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS (If the actual resource requirement are null, filter assign fake resource requirement, so there is a stop and a start.)
    -   IRP\_MN\_STOP\_DEVICE
    -   IRP\_MN\_START\_DEVICE (The filter fails this IRP while going up. This action causes the surprise remove IRP.)
    -   IRP\_MN\_SURPRISE\_REMOVAL
    -   IRP\_MN\_REMOVE

    After the rebalance test is complete, the device will be uninstalled and reenumerated, also removing the filter driver from the stack.

## Device Error Codes


If the test gives an error message saying that the device status is not OK, you can learn more about the device status through Device Manager. For a summary of the various device error codes, see [Device Manager Error Messages](https://msdn.microsoft.com/library/windows/hardware/ff541422).

## Debug installation failures using the Setup API logs


The Setup API logs (setupapi.app.log and setupapi.dev.log) might contain useful information to debug driver installation failures logged by this test. The Setup API logs can be found under %windir%\\inf\\ directory on the test system.

To increase the verbosity and potential usefulness of these logs, set the following registry key to 0x2000FFFF before running the Reinstall test:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Setup\LogLevel
```

## Related topics


[How to How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime)

[How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Device Fundamentals Tests](device-fundamentals-tests.md)

[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398)

[How to test a driver at runtime from a Command Prompt](https://msdn.microsoft.com/windows-drivers/develop/how_to_test_a_driver_at_runtime_from_a_command_prompt)

 

 






