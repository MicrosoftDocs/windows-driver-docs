# Updating Device Firmware

This topic describes how to update your device's firmware using the Windows Update (WU) service. You might need to do this if you are using a Microsoft-supplied class driver for your device.

To update the device's firmware, you'll need to create an additional physical device object (PDO). You can do this by providing an extension INF file that specifies the [AddComponent](../install/inf-addcomponent-directive.md) directive.

We recommend providing a UMDF driver that does the following:

1. At entry point, check the device's firmware version.
2. If an update is required, schedule an update by setting an event timer.
3. Submit your firmware update package as a separate driver submission.

For information about updating chassis-mounted devices, see [Windows UEFI firmware update platform](../bringup/windows-uefi-firmware-update-platform.md)

<!--crunch history before merging to master
I'm not quite clear on the scope of what they'll need to provide.

They're going to provide an extensible INF (that specifies AddComponent), and (ideally) UMDF code that checks the firmware version and schedules an event for the actual update.

Does this mean it's actually a full driver package they'll submit?  And is the updated firmware code encapulated in there in some form?


-->