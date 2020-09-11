---
description: If you are building a new system, the tests in this topic are recommended.
title: Recommended USB tests for system development
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Recommended USB tests for system development


If you are building a new system, the tests in this topic are recommended.

To run DF tests listed in this topic, you must have [MUTT devices](microsoft-usb-test-tool--mutt--devices.md). Depending on the stage, you will need to update driver for the device by running this command:

`muttutil -updatedriver <driver_inf>.inf`

The [MuttUtil](muttutil.md) tool is included in the [MUTT software package](mutt-software-package.md).

If you are building a new system, here are the recommended USB HCK tests:

## Stage 1—System bring-up


-   [DF – Sleep with IO Before and After (Basic)](/previous-versions/windows/hardware/hck/dn247481(v=vs.85))
-   [DF - PNP (disable and enable) with IO Before and After (Basic)](/previous-versions/windows/hardware/hck/dn260411(v=vs.85))
-   [USB Exposed Port controller Test](/previous-versions/windows/hardware/hck/hh998021(v=vs.85))
-   [USB xHCI Transfer Speed Test](/previous-versions/windows/hardware/hck/hh997864(v=vs.85))
-   [USB3 Termination](/previous-versions/windows/hardware/hck/jj124672(v=vs.85))

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
<strong>Note</strong>  To quickly find the controller, type "xhci" in search.
</div>
<div>
 
</div></li>
<li>From the <strong>View By</strong> list, choose <strong>Basic</strong>.</li>
<li>Run the recommended for the selected controller.</li>
</ol></td>
</tr>
</tbody>
</table>

 

## Stage 2—System integration


-   [DF - Reboot restart with IO before and after (Functional)](/previous-versions/windows/hardware/hck/dn260266(v=vs.85))
-   [DF - Sleep and PNP (disable and enable) with IO Before and After (Functional)](/previous-versions/windows/hardware/hck/dn260391(v=vs.85))
-   [USB xHCI Transfer Speed Test](/previous-versions/windows/hardware/hck/hh997864(v=vs.85))

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
<strong>Note</strong>  To quickly find the controller, type "xhci" in search.
</div>
<div>
 
</div></li>
<li>From the <strong>View By</strong> list, choose <strong>Functional</strong>.</li>
<li>Run the recommended for the selected controller.</li>
</ol></td>
</tr>
</tbody>
</table>

 

## Stage 3—System tuneup


System 1

-   [DF - Sleep with IO During (Certification)](/previous-versions/windows/hardware/hck/dn247416(v=vs.85))
-   [DF - Concurrent Hardware And Operating System (CHAOS) Test (Certification)](/previous-versions/windows/hardware/hck/hh998603(v=vs.85))

System 2

-   [DF - Sleep and PNP (disable and enable) with IO Before and After (Functional)](/previous-versions/windows/hardware/hck/dn260391(v=vs.85))
-   [USB xHCI Transfer Speed Test](/previous-versions/windows/hardware/hck/hh997864(v=vs.85))

System 3 (if dock supported)

-   Run the tests listed for the [system integration stage](#stage-2system-integration) on the docked system.

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
<p>See <a href="#stage-1system-bring-up" data-raw-source="[system bring-up topology](#stage-1system-bring-up)">system bring-up topology</a>.</p>
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
<p>See <a href="#stage-2system-integration" data-raw-source="[system integration stage](#stage-2system-integration)">system integration stage</a>.</p></td>
<td><p>System 1</p>
<ol>
<li>On the <strong>Selection</strong> tab, click <strong>Device manager</strong>.</li>
<li>Select the xHCI controller and its root hub.
<div class="alert">
<strong>Note</strong>  To quickly find the controller, type "xhci" in search.
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
<strong>Note</strong>  To quickly find the controller, type "MUTT" in search.
</div>
<div>
 
</div></li>
<li>From the <strong>View By</strong> list, choose <strong>Functional</strong>.</li>
<li>Run the recommended tests for system 2.</li>
<li>Use 2 meter long cables to connect hubs to the system.</li>
</ol>
<p>System 3</p>
<ul>
<li><p>Same as <a href="#stage-2system-integration" data-raw-source="[system integration topology](#stage-2system-integration)">system integration topology</a>.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

## Related topics
[Windows Hardware Lab Kit Tests for USB](windows-hardware-certification-kit-tests-for-usb.md)