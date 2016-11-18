---
title: Device Fundamentals Tests
description: .
ms.assetid: 1963B6BD-158C-4946-8FBA-55DE0C98BE44
---

# Device Fundamentals Tests


## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[CHAOS Tests (Device Fundamentals)](chaos-tests--device-fundamentals-.md)</p></td>
<td align="left"><p>The CHAOS (Concurrent Hardware and Operating System) tests run various PnP driver tests, device driver fuzz tests, and power system tests concurrently.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Coverage Tests (Device Fundamentals)](coverage-tests--device-fundamentals-.md)</p></td>
<td align="left"><p>The Device Fundamental Coverage tests monitor and report on the various I/O request packets (IRPs) that enter or leave a driver stack for specified devices. The data from the Coverage tests can help identify coverage weaknesses during driver test and verification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[CPUStress Tests (Device Fundamentals)](cpustress-tests--device-fundamentals-.md)</p></td>
<td align="left"><p>The CpuStress tests perform device I/O testing with different processor utilization levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[DriverInstall Tests (Device Fundamentals)](driverinstall-tests--device-fundamentals-.md)</p></td>
<td align="left"><p>The Driver Install test category includes tests that uninstall and reinstall a driver several times to test install functionality. The tests initiate I/O testing against the driver and device after each reinstall. The tests are designed to improve the overall experience for end users who need to install and reinstall a device driver or a device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[I/O Tests (Device Fundamentals)](i-o-tests--device-fundamentals-.md)</p></td>
<td align="left"><p>The Device Fundamentals I/O tests perform basic I/O testing on the specified devices.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Penetration Tests (Device Fundamentals)](penetration-tests--device-fundamentals-.md)</p></td>
<td align="left"><p>The Device Fundamentals Penetration tests perform various forms of input attacks, which are a critical component of security testing. Attack and Penetration testing can help identify vulnerabilities in software interfaces.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[PnP Tests (Device Fundamentals)](pnp-tests--device-fundamentals-.md)</p></td>
<td align="left"><p>The Device Fundamentals PnP tests force a driver to handle almost all of the PnP IRPs; however, there are three areas that are stressed specifically: removal, rebalance, and surprise removal. The PnP test provides a mechanism to test each of these separately, or to test them all together (that is, as a stress test). This PnP testing is accomplished by using a combination of user-mode API calls (through the test application) and kernel-mode API calls (through an upper-filter driver).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Reboot Tests (Device Fundamentals)](reboot-tests--device-fundamentals-.md)</p></td>
<td align="left"><p>The Device Fundamentals Reboot tests run I/O on the specified devices, before and after, or during system restarts.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Sleep Tests (Device Fundamentals)](sleep-tests--device-fundamentals-.md)</p></td>
<td align="left"><p>The Device Fundamentals Sleep tests run I/O and PnP operations on the specified devices, before and after, or during system sleep state transitions. The Sleep tests ensure that the device under test permits the system to be cycled through all of the supported sleep states. Additionally, it ensures that the device is still functional after these state changes through Simple I/O stress testing.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Device%20Fundamentals%20Tests%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




