---
Description: Possible causes and resolutions to troubleshooting messages in Windows 10 that users might get on USB Type-C systems running Windows.
title: Troubleshoot messages for a USB Type-C Windows system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshoot messages for a USB Type-C Windows system


Possible causes and resolutions to troubleshooting messages in Windows 10 that users might get on USB Type-C systems running Windows.

The symmetric and reversible design of the USB Type-C connector allows users to connect systems running Windows to connect any USB Type-C device, and use new features such as enhanced charging and alternate modes. However, certain combinations of hardware and/or software limitations might prevent some of these features from functioning properly. Windows 10 provides a set of USB Type-C notifications to help users troubleshoot these issues.

In this topic, a USB Type-C system refers to a PC running Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) or a mobile device running Windows 10 Mobile.

**Troubleshooting messages related to USB Type-C connectors of a system**

-   [You might be able to fix your USB device](#-1)
-   [Device is charging slowly](#-2)
-   [The USB device might not work](#-3)
-   [Try improving the USB connection](#-4)
-   [Display connection is limited](#-5)
-   [These two PCs (mobile devices) can't communicate](#-6)

## <a href="" id="-1"></a>You might be able to fix your USB device


**Your USB device ran into a problem. Follow these steps to try to fix it. (Error code \_\_\_\_) **

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Possible cause</th>
<th>Recommended resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The device hardware reported a problem or the device driver is faulty.</p></td>
<td><ol>
<li>Note the error code.
<ul>
<li>On Windows 10 for desktop editions systems, open Device Manager and find the device. It&#39;s marked with a yellow exclamation point. Right-click on the node and open device properties. The error code is under <strong>Device status</strong>.</li>
<li>On Windows 10 Mobile systems, the notification shows the error code.</li>
</ul></li>
<li>Follow the troubleshooting steps described in <a href="http://go.microsoft.com/fwlink/p/?LinkId=526896" data-raw-source="[this article](http://go.microsoft.com/fwlink/p/?LinkId=526896)">this article</a>.</li>
</ol>
<div class="alert">
<strong>Note</strong>  Applies to all error codes shown in Device Manager except for Code 28.
</div>
<div>

</div></td>
</tr>
</tbody>
</table>



## <a href="" id="-2"></a>Device is charging slowly


**To speed up charging, use the charger and cable that came with your device.**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Possible causes</th>
<th>Recommended resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li>The charger is not compatible with your system.
<div class="alert">
<strong>Note</strong>  Non-USB Type-C chargers support the USB Battery Charging 1.2 specification. Some of these chargers use proprietary charging mechanisms. Your system might not support all those chargers.
</div>
<div>

</div></li>
<li>The charger is not powerful enough to charge the system.</li>
<li>The charger is not connected to a charging port of the system.</li>
<li>The charging cable does not meet the power requirement of the charger or the system.</li>
</ul>
<div class="alert">
<strong>Note</strong><br/><p>A system with USB Type-C connectors has higher power limits, it can support up to 5V, 3A, 15W. If the connector supports <a href="http://go.microsoft.com/fwlink/p/?LinkID=623310" data-raw-source="[USB Power Delivery](http://go.microsoft.com/fwlink/p/?LinkID=623310)">USB Power Delivery</a> (industry standard), it can charge faster at higher power levels.</p>
<p>In order for you to get the fast charging benefits, your system, charger, and cable must support the industry standards. In addition, your charger and cable must support the power levels required by the system to optimally charge it. For example, if your system requires 12V and 3A for charging, a 5V, 3A charger cannot charge your system optimally.</p>
</div>
<div>

</div></td>
<td><ul>
<li>Use the charger and cable that came with your device.</li>
<li>Make sure that you&#39;re connecting your charger to the charging USB Type-C port on your system.</li>
</ul></td>
</tr>
</tbody>
</table>



## <a href="" id="-3"></a>The USB device might not work


**Try connecting it to a PC.**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Possible cause</th>
<th>Recommended resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The driver for the connected device is not supported on the version of Windows running on the system. For information about the supported devices, see <a href="supported-usb-classes.md" data-raw-source="[USB device class drivers included in Windows](supported-usb-classes.md)">USB device class drivers included in Windows</a>.</p>
<div class="alert">
<strong>Note</strong>  A mobile system has the capability to connect with other USB peripherals. However, not all devices that connect to a PC can connect to a mobile system. Check the preceding list to the supported devices.
</div>
<div>

</div></td>
<td><ul>
<li>Make sure that you are running the latest version of Windows so that you have most recent driver packages. For information, see <a href="http://go.microsoft.com/fwlink/p/?LinkID=698739" data-raw-source="[Windows 10 Updates](http://go.microsoft.com/fwlink/p/?LinkID=698739 )">Windows 10 Updates</a>.</li>
<li>If you are already running the latest version, try connecting your device to a PC instead.</li>
</ul></td>
</tr>
</tbody>
</table>



## <a href="" id="-4"></a>Try improving the USB connection


**Make sure the device you are connecting to is supported and you are using the right cable.**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Possible cause</th>
<th>Recommended resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li>You have connected a device with new USB Type-C features that not supported by your system.</li>
<li>You have connected a device with new USB Type-C features that is not supported by the cable.</li>
</ul>
<p>USB Type-C introduces a new feature called alternate modes, which allows non-USB protocols to run over the USB Type-C cable. For example, a dock that uses alternate modes has the ability to transmit a video signal over USB.</p>
<p>In order for an alternate mode to work, the hardware and the software on the PC/phone and the device or adapter must support the alternate mode. In addition, certain alternate modes may require specific USB Type-C cables.</p></td>
<td><ul>
<li>Make sure your system supports the features of the connected device.</li>
<li>Make sure your cable supports the features of the connected device.</li>
</ul></td>
</tr>
</tbody>
</table>



## <a href="" id="-5"></a>Display connection is limited


**DisplayPort/MHL connection might not work. Try using a different cable.**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Possible cause</th>
<th>Recommended resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li>You have connected a device with new USB Type-C features that are not supported by your system.</li>
<li>You have connected a device with new USB Type-C features that are not supported by the cable.</li>
</ul>
<p>USB Type-C introduces a new feature called alternate modes. The feature allows non-USB protocols to run over the USB Type-C cable, while simultaneously preserving USB 2.0 and charging functionality. Here are the display alternate modes:</p>
<ul>
<li><p><strong>DisplayPort</strong> /<strong>DockPort</strong></p>
<p>This alternate mode allows the user to project audio/video to external DisplayPort displays over a USB connector.</p></li>
<li><p><strong>MHL</strong></p>
<p>The MHL alternate mode is allows the user to project video/audio to external displays that support MHL.</p></li>
</ul>
<p>The hardware and software on the system, the device or adapter, or cable does not support the <strong>DisplayPort</strong> /<strong>DockPort</strong> or <strong>MHL</strong> alternate modes.</p></td>
<td><ul>
<li>Make sure the system, device, and cable support <strong>DisplayPort</strong> /<strong>DockPort</strong> or <strong>MHL</strong> alternate modes.</li>
</ul></td>
</tr>
</tbody>
</table>



## <a href="" id="-6"></a>These two PCs (mobile devices) can't communicate


**Try connecting one of them to a mobile device (PC) to achieve your goal.**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Possible cause</th>
<th>Recommended resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li>You cannot connect two PCs running Windows 10 for desktop editions.</li>
<li>You cannot connect two mobile devices running Windows 10 Mobile.</li>
</ul></td>
<td>This connection scenario is not supported.</td>
</tr>
</tbody>
</table>










