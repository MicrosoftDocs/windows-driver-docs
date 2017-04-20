---
Description: If you are building a new system, the tests in this topic are recommended.
title: Recommended USB tests for system development
author: windows-driver-content
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Recommended USB tests for system development


If you are building a new system, the tests in this topic are recommended.

To run DF tests listed in this topic, you must have [MUTT devices](microsoft-usb-test-tool--mutt--devices.md). Depending on the stage, you will need to update driver for the device by running this command:

`muttutil -updatedriver <driver_inf>.inf`

The [MuttUtil](muttutil.md) tool is included in the [MUTT software package](mutt-software-package.md).

If you are building a new system, here are the recommended USB HCK tests:

## <a href="" id="stage1"></a>Stage 1—System bring-up


-   [DF – Sleep with IO Before and After (Basic)](http://msdn.microsoft.com/library/windows/hardware/dn247481.aspx)
-   [DF - PNP (disable and enable) with IO Before and After (Basic)](http://msdn.microsoft.com/library/windows/hardware/dn260411.aspx)
-   [USB xHCI Runtime Power Management](http://msdn.microsoft.com/library/windows/hardware/hh998627.aspx)
-   [USB xHCI Register Test](http://msdn.microsoft.com/library/windows/hardware/jj123677.aspx)
-   [USB Host Controller Enable Disable Test](http://msdn.microsoft.com/library/windows/hardware/jj123757.aspx)
-   [USB Host Controller Compliance](http://msdn.microsoft.com/library/windows/hardware/jj124075.aspx)
-   [USB Exposed Port controller Test](http://msdn.microsoft.com/library/windows/hardware/hh998021.aspx)
-   [USB xHCI Transfer Speed Test](http://msdn.microsoft.com/library/windows/hardware/hh997864.aspx)
-   [USB3 Termination](http://msdn.microsoft.com/library/windows/hardware/jj124672.aspx)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>For each xHCI controller on the system, configure this topology</th>
<th>Running the recommended test</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol>
<li>Connect a USB 3.0 hub to a SuperSpeed port of the system.</li>
<li><p>Connect a SuperMUTT downstream of the USB 3.0 hub.</p>
<p></p>
<p><strong>Device driver:  </strong>The SuperMUTT device must have Winusb.sys as the device driver. Run this command:</p>
<p><code>muttutil -updatedriver usbfx2.inf</code></p>
<p><img src="images/xhci-superspeedhub-supermutt.png" alt="System bring-up topology" /></p></li>
</ol>
<div class="alert">
<strong>Note</strong>  If system does not have a Type A connector, then an adapter should be included with the system.
</div>
<div>
 
</div></td>
<td><ol>
<li>In Windows HCK Studio, on the <strong>Selection</strong> tab, click <strong>Device manager</strong>.</li>
<li>Select the xHCI controller and its root hub.
<div class="alert">
<strong>Note</strong>  To quickly find the controller, type &quot;xhci&quot; in search.
</div>
<div>
 
</div></li>
<li>From the <strong>View By</strong> list, choose <strong>Basic</strong>.</li>
<li>Run the recommended for the selected controller.</li>
</ol></td>
</tr>
</tbody>
</table>

 

## <a href="" id="stage2"></a>Stage 2—System integration


-   [DF - Reboot restart with IO before and after (Functional)](http://msdn.microsoft.com/library/windows/hardware/dn260266.aspx)
-   [DF - Sleep and PNP (disable and enable) with IO Before and After (Functional)](http://msdn.microsoft.com/library/windows/hardware/dn260391.aspx)
-   [USB xHCI Transfer Speed Test](http://msdn.microsoft.com/library/windows/hardware/hh997864.aspx)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>For each xHCI controller on the system, configure this topology</th>
<th>Running the recommended test</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p></p>
<p>For each xHCI controller on the system, configure this topology</p>
<ol>
<li>Connect a USB 3.0 hub to a SuperSpeed port of the system.</li>
<li><p>Connect a SuperMUTT downstream of the USB 3.0 hub.</p>
<p><strong>Device driver:  </strong>The SuperMUTT device must have Usbtcd.sys as the device driver. Run this command:</p>
<p><code>muttutil -updatedriver usbtcd.inf</code></p></li>
<li>Connect a SuperMUTT Pack downstream of the USB 3.0 hub.</li>
</ol>
<p><img src="images/xhci-system-integration.png" alt="System integration topology" /></p>
<p></p>
<div class="alert">
<strong>Note</strong>  If system does not have a Type A connector, then an adapter should be included with the system.
</div>
<div>
 
</div></td>
<td><p>To run the tests:</p>
<ol>
<li>On the <strong>Selection</strong> tab, click <strong>Device manager</strong>.</li>
<li>Select the xHCI controller and its root hub.
<div class="alert">
<strong>Note</strong>  To quickly find the controller, type &quot;xhci&quot; in search.
</div>
<div>
 
</div></li>
<li>From the <strong>View By</strong> list, choose <strong>Functional</strong>.</li>
<li>Run the recommended for the selected controller.</li>
</ol></td>
</tr>
</tbody>
</table>

 

## <a href="" id="stage3"></a>Stage 3—System tuneup


System 1

-   [DF - Sleep with IO During (Certification)](http://msdn.microsoft.com/library/windows/hardware/dn247416.aspx)
-   [DF - Concurrent Hardware And Operating System (CHAOS) Test (Certification)](http://msdn.microsoft.com/library/windows/hardware/hh998603.aspx)

System 2

-   [DF - Sleep and PNP (disable and enable) with IO Before and After (Functional)](http://msdn.microsoft.com/library/windows/hardware/dn260391.aspx)
-   [USB xHCI Transfer Speed Test](http://msdn.microsoft.com/library/windows/hardware/hh997864.aspx)

System 3 (if dock supported)

-   Run the tests listed for the [system integration stage](#stage2) on the docked system.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>For each xHCI controller on the system, configure this topology</th>
<th>Running the recommended test</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>System 1</p>
<p>See [system bring-up topology](#stage1).</p>
<p><strong>Device driver:  </strong>The SuperMUTT device must have Usbtcd.sys as the device driver. Run this command:</p>
<p><code>muttutil -updatedriver usbtcd.inf</code></p>
<p>System 2</p>
<p>For each xHCI controller on the system, configure this topology</p>
<ol>
<li>Connect a USB 3.0 hub to a SuperSpeed port of the system.</li>
<li>Connect a SuperMUTT downstream of the USB 3.0 hub.</li>
<li>Connect a SuperMUTT Pack downstream of the USB 3.0 hub.</li>
<li>Connect a MUTT Pack downstream of the USB 3.0 hub.</li>
<li>Connect four self-powered USB 3.0 hubs downstream of each other (forming a chain) with the first hub downstream of the SuperMUTT Pack.</li>
<li>Connect a MUTT (or a SuperMUTT Pack) downstream of the last USB 3.0 hub in the chain.</li>
</ol>
<img src="images/xhci-superspeedhub-hub-daisy.png" alt="System tuning topology" />
<p>System 3 (if dock supported)</p>
<p>See [system integration stage](#stage2).</p></td>
<td><p>System 1</p>
<ol>
<li>On the <strong>Selection</strong> tab, click <strong>Device manager</strong>.</li>
<li>Select the xHCI controller and its root hub.
<div class="alert">
<strong>Note</strong>  To quickly find the controller, type &quot;xhci&quot; in search.
</div>
<div>
 
</div></li>
<li>From the <strong>View By</strong> list, choose <strong>Certification</strong>.</li>
<li>Run the recommended for the selected controller.</li>
</ol>
<p>System 2</p>
<ol>
<li>On the <strong>Selection</strong> tab, click <strong>Device manager</strong>.</li>
<li>Select all MUTT devices in the topology, shown in the list.
<div class="alert">
<strong>Note</strong>  To quickly find the controller, type &quot;MUTT&quot; in search.
</div>
<div>
 
</div></li>
<li>From the <strong>View By</strong> list, choose <strong>Functional</strong>.</li>
<li>Run the recommended tests for system 2.</li>
<li>Use 2 meter long cables to connect hubs to the system.</li>
</ol>
<p>System 3</p>
<ul>
<li><p>Same as [system integration topology](#stage2).</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

## Related topics
[Windows Hardware Certification Kit Tests for USB](windows-hardware-certification-kit-tests-for-usb.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Recommended%20USB%20tests%20for%20system%20development%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


