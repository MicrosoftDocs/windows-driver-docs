---
title: Recommended USB tests for system development
description: If you're building a new system, the tests in this article are recommended.
ms.date: 03/08/2023
---

# Recommended USB tests for system development

If you're building a new system, the tests in this article are recommended.

To run DF tests listed in this article, you must have [MUTT devices](microsoft-usb-test-tool--mutt--devices.md). Depending on the stage, you'll need to update driver for the device by running this command:

`muttutil -updatedriver <driver_inf>.inf`

The [MuttUtil](muttutil.md) tool is included in the [MUTT software package](mutt-software-package.md).

If you're building a new system, here are the recommended USB HCK tests:

## Stage 1—System bring-up

- [DF – Sleep with IO Before and After (Basic)](/previous-versions/windows/hardware/hck/dn247481(v=vs.85))
- [DF - PNP (disable and enable) with IO Before and After (Basic)](/previous-versions/windows/hardware/hck/dn260411(v=vs.85))
- [USB Exposed Port controller Test](/previous-versions/windows/hardware/hck/hh998021(v=vs.85))
- [USB xHCI Transfer Speed Test](/previous-versions/windows/hardware/hck/hh997864(v=vs.85))
- [USB3 Termination](/previous-versions/windows/hardware/hck/jj124672(v=vs.85))

| For each xHCI controller on the system, configure this topology | Running the recommended test |
|---|---|
| <ol><li>Connect a USB 3.0 hub to a SuperSpeed port of the system.</li><li>Connect a SuperMUTT downstream of the USB 3.0 hub.<br><br>**Device driver:** The SuperMUTT device must have Winusb.sys as the device driver. Run this command:<br><br>`muttutil -updatedriver usbfx2.inf`<br><br>:::image type="content" source="images/xhci-superspeedhub-supermutt.png" alt-text="Diagram of system bring-up topology.":::<br>If system doesn't have a Type A connector, then an adapter should be included with the system.</li></ol> | <ol><li>In Windows HCK Studio, on the **Selection** tab, select **Device Manager**.</li><li>Select the xHCI controller and its root hub. To quickly find the controller, type "xhci" in search.</li><li>From the **View By** list, choose **Basic**.</li><li>Run the recommended test for the selected controller.</li></ol> |

## Stage 2—System integration

- [DF - Reboot restart with IO before and after (Functional)](/previous-versions/windows/hardware/hck/dn260266(v=vs.85))
- [DF - Sleep and PNP (disable and enable) with IO Before and After (Functional)](/previous-versions/windows/hardware/hck/dn260391(v=vs.85))
- [USB xHCI Transfer Speed Test](/previous-versions/windows/hardware/hck/hh997864(v=vs.85))

| For each xHCI controller on the system, configure this topology | Running the recommended test |
|---|---|
| For each xHCI controller on the system, configure this topology<br><ol><li>Connect a USB 3.0 hub to a SuperSpeed port of the system.</li><li>Connect a SuperMUTT downstream of the USB 3.0 hub.<br><br>**Device driver:** The SuperMUTT device must have Usbtcd.sys as the device driver. Run this command:<br><br>`muttutil -updatedriver usbtcd.inf`<br><br>Connect a SuperMUTT Pack downstream of the USB 3.0 hub.:::image type="content" source="images/xhci-system-integration.png" alt-text="Diagram of system integration topology.":::<br>If system doesn't have a Type A connector, then an adapter should be included with the system. | To run the tests:<br><ol><li>On the **Selection** tab, select **Device manager**.</li><li>Select the xHCI controller and its root hub.<br>To quickly find the controller, type "xhci" in search.</li><li>From the **View By** list, choose **Functional**.</li><li>Run the recommended test for the selected controller.</li></ol> |

## Stage 3—System tune up

System 1

- [DF - Sleep with IO During (Certification)](/previous-versions/windows/hardware/hck/dn247416(v=vs.85))
- [DF - Concurrent Hardware And Operating System (CHAOS) Test (Certification)](/previous-versions/windows/hardware/hck/hh998603(v=vs.85))

System 2

- [DF - Sleep and PNP (disable and enable) with IO Before and After (Functional)](/previous-versions/windows/hardware/hck/dn260391(v=vs.85))
- [USB xHCI Transfer Speed Test](/previous-versions/windows/hardware/hck/hh997864(v=vs.85))

System 3 (if dock supported)

- Run the tests listed for the [system integration stage](#stage-2system-integration) on the docked system.

| For each xHCI controller on the system, configure this topology | Running the recommended test |
|---|---|
| System 1<br><br>See [system bring-up topology](#stage-1system-bring-up).<br><br>**Device driver:** The SuperMUTT device must have Usbtcd.sys as the device driver. Run this command:<br>`muttutil -updatedriver usbtcd.inf`<br><br>System 2<br><br>For each xHCI controller on the system, configure this topology<br><ol><li>Connect a USB 3.0 hub to a SuperSpeed port of the system.</li><li>Connect a SuperMUTT downstream of the USB 3.0 hub.</li><li>Connect a SuperMUTT Pack downstream of the USB 3.0 hub.</li><li>Connect a MUTT Pack downstream of the USB 3.0 hub.</li><li>Connect four self-powered USB 3.0 hubs downstream of each other (forming a chain) with the first hub downstream of the SuperMUTT Pack.</li><li>Connect a MUTT (or a SuperMUTT Pack) downstream of the last USB 3.0 hub in the chain.</li></ol>:::image type="content" source="images/xhci-superspeedhub-hub-daisy.png" alt-text="Diagram of system tuning topology.":::<br>System 3 (if dock supported)<br><br>See [system integration stage](#stage-2system-integration). | System 1<br><ol><li>On the **Selection** tab, select **Device manager**.</li><li>Select the xHCI controller and its root hub.</li><li>To quickly find the controller, type "xhci" in search.</li><li>From the **View By** list, choose **Certification**.</li><li>Run the recommended test for the selected controller.</li></ol><br>System 2<br><ol><li>On the **Selection** tab, select **Device manager**.</li><li>Select all MUTT devices in the topology, shown in the list.<br>To quickly find the controller, type "MUTT" in search.</li><li>From the **View By** list, choose **Functional**.</li><li>Run the recommended tests for system 2.</li><li>Use 2-meter long cables to connect hubs to the system.</li></ol><br>System 3<br></ul><li>Same as [system integration topology](#stage-2system-integration).</li></ul> |

## Related topics

- [Windows Hardware Lab Kit Tests for USB](windows-hardware-certification-kit-tests-for-usb.md)
