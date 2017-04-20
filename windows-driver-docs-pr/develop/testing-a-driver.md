---
ms.assetid: bb73768e-0ac9-4377-9caa-c0cce1d10bb8
title: Testing a Driver
description: Testing a Driver
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Testing a Driver

The WDK adds a driver testing interface to Visual Studio that allows you to conveniently build, deploy, install, and test a driver on a remote test computer on your network. The WDK also provides a collection of device driver tests that you can use to test features and functions of your driver. You can also write customize or write your own driver tests using the Driver Test Template in Visual Studio.

## <span id="Video_Demonstration"></span><span id="video_demonstration"></span><span id="VIDEO_DEMONSTRATION"></span>Video Demonstration


This video demonstrates the how to run driver-related tests in a test group.

<iframe 
src="https://hubs-video.ssl.catalog.video.msn.com/embed/e12e5ce5-b41f-4b91-ab5f-69598ccdcb57/IA?csid=ux-en-us&MsnPlayerLeadsWith=html&PlaybackMode=Inline&MsnPlayerDisplayShareBar=false&MsnPlayerDisplayInfoButton=false&iframe=true&QualityOverride=HD" width="720" height="405" allowFullScreen="true" frameBorder="0" scrolling="no"></iframe> 

This section describes some strategies for testing driver, and information about how you select and configure a remote computer to use for testing.

To prepare a driver for public distribution, you should run the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893). For information about the Windows Certification program and how to obtain the HCK, see [Windows Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016).
## 
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
<td align="left"><p>[Tips for testing drivers during development](strategies-for-testing-drivers-during-development.md)</p></td>
<td align="left"><p><strong>When should you start testing?</strong> As soon as you have the requirements for your driver, you can begin to design test cases to test that the critical requirements have been implemented. Studies show that finding and fixing defects in code becomes more expensive the longer the defects remain in the code. Finding and fixing defects early in the development cycle is less costly and disruptive than finding defects after the code has been released and distributed. Creating your test cases early can also help you find problems in your design.</p>
<p></p></td>
</tr>
<tr class="even">
<td align="left"><p>[How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md)</p></td>
<td align="left"><p>The WDK extensions to Visual Studio provide a device testing interface that enables you to conveniently build, deploy, install, and test a driver on a test computer on your network. The WDK provides a collection of device driver tests that you can use to test the features and functions of your driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[How to write a driver test using a Driver Test template](how-to-write-a-driver-test-.md)</p></td>
<td align="left"><p>You can use the Windows Driver Kit (WDK) for Windows 8 to create your own driver tests or to customize some of the tests that are provided. You can deploy the tests that you create to remote test computers using the driver testing framework that the WDK provides for Microsoft Visual Studio Ultimate 2012.</p></td>
</tr>
</tbody>
</table>

 

 

 





