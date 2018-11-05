---
ms.assetid: bb73768e-0ac9-4377-9caa-c0cce1d10bb8
title: Testing a Driver
description: Testing a Driver
ms.date: 06/28/2018
ms.localizationpriority: medium
---

# Testing a Driver

The WDK adds a driver testing interface to Visual Studio that allows you to build, deploy, install, and test a driver on a remote test computer on your network. The WDK also provides a collection of device driver tests that you can use to test features and functions of your driver. You can also write customize or write your own driver tests using the Driver Test Template in Visual Studio.

## <span id="Video_Demonstration"></span><span id="video_demonstration"></span><span id="VIDEO_DEMONSTRATION"></span>Video Demonstration


This video demonstrates the how to run driver-related tests in a test group.

<iframe class="video-iframe" style="width: 100%; height: 550px;" frameborder="0" allowfullscreen="true" src ="https://www.microsoft.com/videoplayer/embed/e12e5ce5-b41f-4b91-ab5f-69598ccdcb57?autoplay=false"></iframe> 

This section describes some strategies for testing driver, and information about how you select and configure a remote computer to use for testing.

To prepare a driver for public distribution, you should run the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893). For information about the Windows Certification program and how to obtain the HCK, see [Windows Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016).

The WDK provides the test binaries and tools which make it easy to run the Device Fundamentals tests from the command-line.
For more information, see [Run the DevFund Tests via the command-line](https://review.docs.microsoft.com/windows-hardware/drivers/devtest/run-devfund-tests-via-the-command-line).

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
<td align="left"><p><a href="strategies-for-testing-drivers-during-development.md" data-raw-source="[Tips for testing drivers during development](strategies-for-testing-drivers-during-development.md)">Tips for testing drivers during development</a></p></td>
<td align="left"><p><strong>When should you start testing?</strong> As soon as you have the requirements for your driver, you can begin to design test cases to test that the critical requirements have been implemented. Studies show that finding and fixing defects in code becomes more expensive the longer the defects remain in the code. Finding and fixing defects early in the development cycle is less costly and disruptive than finding defects after the code has been released and distributed. Creating your test cases early can also help you find problems in your design.</p>
<p></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="testing-a-driver-at-runtime.md" data-raw-source="[How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md)">How to test a driver at runtime using Visual Studio</a></p></td>
<td align="left"><p>The WDK extensions to Visual Studio provide a device testing interface that enables you to conveniently build, deploy, install, and test a driver on a test computer on your network. The WDK provides a collection of device driver tests that you can use to test the features and functions of your driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="how-to-write-a-driver-test-.md" data-raw-source="[How to write a driver test using a Driver Test template](how-to-write-a-driver-test-.md)">How to write a driver test using a Driver Test template</a></p></td>
<td align="left"><p>You can use the Windows Driver Kit (WDK) for Windows 8 to create your own driver tests or to customize some of the tests that are provided. You can deploy the tests that you create to remote test computers using the driver testing framework that the WDK provides for Microsoft Visual Studio Ultimate 2012.</p></td>
</tr>
</tbody>
</table>

 

 

 





