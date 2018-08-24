---
title: Device Fundamentals Tests
description: Descriptions of device fundamental tests.
ms.assetid: 1963B6BD-158C-4946-8FBA-55DE0C98BE44
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 

 





