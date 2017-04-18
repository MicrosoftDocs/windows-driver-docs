---
title: CHAOS Tests (Device Fundamentals)
description: The CHAOS (Concurrent Hardware and Operating System) tests run various PnP driver tests, device driver fuzz tests, and power system tests concurrently.
ms.assetid: FA0D73DC-B0B8-4CA7-8DDC-A2C3EC106C3F
---

# CHAOS Tests (Device Fundamentals)


The CHAOS (Concurrent Hardware and Operating System) tests run various PnP driver tests, device driver fuzz tests, and power system tests concurrently.

### <span id="coverage_tests"></span><span id="COVERAGE_TESTS"></span>CHAOS Tests

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
<p>The PnP driver test uses EDT filter driver to send IRP_MN_CANCEL_REMOVE_DEVICE to target device stacks.</p>
<p><strong>Parameters:</strong> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
<p><em>DQ</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Run_CHAOS_Test"></span><span id="run_chaos_test"></span><span id="RUN_CHAOS_TEST"></span>Run CHAOS Test</p></td>
<td align="left"><p>Runs PnP testing and Fuzz testing in parallel while cycling the system through all supported system power states. The PnP driver tests send I/O requests to target device stacks while performing PnP operations.</p>
<p>This test the runs PnP tests (disable/enable, rebalance, remove/restart, surprise remove, and DIF remove) and Driver Fuzz tests on the test device in parallel, while cycling the test system in and out of all of its supported sleep states (S1, S2, S3, S4 and Connected Standby) at the same time. The goal of this test is to test PNP, I/O, and Power concurrency scenarios and find any crashes and/or hangs in the process.</p>
<p><strong>Test binary:</strong> Devfund_ChaosTest.dll</p>
<p><strong>Test method:</strong> RunCHAOSTest</p>
<p><strong>Parameters:</strong></p>
<p><em>DQ</em> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
<p><em>TestPeriod</em> - Specifies how long to run the test (in minutes).</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[How to How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime)

[How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Device Fundamentals Tests](device-fundamentals-tests.md)

[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[PwrTest](pwrtest.md)

[Penetration Tests (Device Fundamentals)](penetration-tests--device-fundamentals-.md)

[PnP Tests (Device Fundamentals)](pnp-tests--device-fundamentals-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20CHAOS%20Tests%20%28Device%20Fundamentals%29%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





