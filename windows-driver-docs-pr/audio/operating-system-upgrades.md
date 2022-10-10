---
title: Operating System Upgrades
description: Operating System Upgrades
keywords:
- audio adapters WDK , operating system upgrades
- adapter drivers WDK audio , operating system upgrades
- Port Class audio adapters WDK , operating system upgrades
- preserving audio settings WDK audio
- CAPX settings framework
- migrating settings WDK audio
ms.date: 09/09/2022
---

# Operating System Upgrades

An audio device's driver settings can frequently be preserved across operating system upgrades. After the upgrade, the goal is to move user settings forward, while also ensuring that the audio endpoints accurately reflect the OS and driver capabilities.

## Audio endpoint migration process

During OS upgrades, an audio end point migration process may run. This process attempts to move as much information forward that is safe to do so. As you develop your audio driver, keep these migration behaviors in mind.

This endpoint migration process can run in the following situations.

- OS update.
- Audio Driver updates. This includes installing an audio extension driver or an AudioProcessingObject. For more information, see [Creating a componentized audio driver installation](audio-universal-drivers.md#creating-a-componentized-audio-driver-installation).
- The existing audio driver is reinstalled in place. This reinstallation can occur when the audio troubleshooter is run. This can also occur through the device manager by doing an "update driver" and selecting the driver that is already installed.
- AudioEndpointBuilder is serviced. This occurs whenever there is a bug fix in the AudioEndpointBuilder service that is updated in released versions of Windows.
- The firmware revision on a USB audio driver is changed.
- The audio driver changes the endpoint configuration via `KSPROPERTY_JACK_DESCRIPTION3`.

### The audio endpoint migration process

The audio endpoint migration process does the following.

- Copies forward user-controlled endpoint properties.
- Copies forward CAPX properties.

The audio endpoint migration process does not do any of the following.

- Does not copy forward FXProperties prior to CAPX availability with Windows 11.
- It does not copy forward Properties that are not in the list of user settings known to the OS.

Starting with Windows 11, a new "CAPX" settings framework is used to store settings. The Settings Framework allows APOs to expose methods for querying and modifying the property store for audio effects ("FX Property Store") on an audio endpoint. For more information, see [Windows 11 APIs for Audio Processing Objects](windows-11-apis-for-audio-processing-objects.md).

### Matching the pre-upgrade endpoints to post upgrade endpoints

The migration process matches the pre-upgrade endpoints to post upgrade endpoints using these two elements.

- *Hardware Id* - For more information about the hardware Id, see [System-Wide Unique Device IDs](system-wide-unique-device-ids.md).
- *Reference string* - The use of the *reference string* is discussed below.

Note that because new endpoints are created, caching mmdevice id's will not work during the end point migration process.

#### Registered Subdevice

The port class driver's [PcRegisterSubdevice function](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregistersubdevice) registers the subdevice, which is perceived as a device by the rest of the system.  The function registers the device interface instance for a filter object that represents a subdevice on an audio adapter. The I/O manager appends the string specified by the Name parameter to the reference string that it uses to identify the instance. The modified reference string is useful for distinguishing among the subdevices in the audio adapter. For more information about reference strings, see [IoRegisterDeviceInterface](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface).

#### Reference string usage

Audio endpoints are identified by the *reference string* passed to PnP when the KS interface was created, along with the pin ID for the external connector. Changing these values will cause a new audio endpoint to be created. This new audio endpoint will not contain the user settings associated to the prior reference string and connector pin ID.

In cases where the hardware id is the same between two or more installed audio devices and the reference strings are also identical, the migration system will not be able to migrate settings properly due to failing to match the endpoints from prior to the migration to the endpoints after the migration.

Installing multiple copies of the same root enumerated software audio devices on all versions of Windows, which all use the same hardware id and reference strings, will not migrate correctly.

#### Prior to Windows 11

For root enumerated software audio devices on systems prior to Windows 11, audio endpoints with the same reference string values will not migrate correctly.

When creating a root enumerated software audio device that targeting Windows versions prior to Windows 11, a unique reference string value needs to be used for each audio endpoint to ensure a successful migration.

#### Windows 11 and later

Root enumerated software audio devices on systems on and after Windows 11, without a hardware id, audio endpoints with the same reference string values will not migrate correctly.

When creating a root enumerated software audio device that targets Windows versions after Windows 11, a unique hardware id needs to be specified in the driver inf, and each root enumerated software audio device can only be installed a single time with that hardware id. To install multiple copies of the same driver, different reference strings must be used on each installation to ensure a successful migration.

### Reference string rules

It is strongly recommended not to use the default "wave" and "topo" reference strings that are used in the audio sample driver(s). More descriptive reference strings should be used instead. Drivers which use the default reference strings have a risk of having their migration data lost or applied to the wrong device in the event that a hardware id is unavailable or matches some other driver using these reference strings. A reasonable strategy would be something like "ContosoSoftwareRender-output2". Including a unique vendor name helps to disambiguate the reference string.

Reference strings must remain static for the audio driver installation, updates, OS updates, reboots, etc. If the reference string changes, a new audio endpoint will be created and user settings will not be copied from the previous endpoint to the new endpoint.

#### Hardware Id Device Instance Name  

The audio driver Hardware Id is defined in the Models section of the INF file. The Hardware Id identifies at least one device, and references the DDInstall section of the INF file for that device. It also specifies a unique-to-the-model-section Hardware identifier (ID) for that device. For more information see, [INF Models section](../install/inf-models-section.md) and [INF DDInstall section](../install/inf-ddinstall-section.md).

This INF file shows the Device Description from the DDInstall section in the Sysvad audio sample.

```inf
[SYSVAD.NT$ARCH$]
%SYSVAD_SA.DeviceDesc%=SYSVAD_SA, Root\sysvad_ComponentizedAudioSample

SYSVAD_SA.DeviceDesc="Virtual Audio Device (WDM) - Tablet Sample"
```

This INF file shows the how the Device Description would be customized by an OEM.

```inf
[CONTOSO.NT$ARCH$]
%CONTOSO_SA.DeviceDesc%=CONTOSO_SA, Root\contoso_ContosoSoftwareRender

CONTOSO_SA.DeviceDesc="Description of the Contoso Software Render Driver"
```

The hardware id that AudioEndpointBuilder will match on would be `Root\contoso_ContosoSoftwareRender`

## Registry stored settings

An audio adapter driver can keep track of its current device settings (chiefly volume levels and mute settings) in the system registry. The driver typically stores these settings in the system-supplied driver key (represented by the INF keyword HKR) under the subkey "Settings". When the user alters these settings through a control panel or other audio application, the driver updates the appropriate registry entries. Each time the system boots, the driver restores the device settings from the registry.

Users largely prefer this behavior because it preserves the adjustments they have made to the system over time instead of forcing them to try to restore their settings manually each time they upgrade the operating system.

Some drivers, however, blindly overwrite these settings with defaults each time they are installed. A better approach is for a driver to determine at installation time whether certain driver-specific entries already exist. If they do exist, the driver should preserve the settings that are contained in these entries instead of overwriting them.

The directives in the add-registry section of the driver's INF file specify whether existing registry entries should be overwritten. For more information, see the description of the FLG\_ADDREG\_NOCLOBBER flag in [**INF AddReg Directive**](../install/inf-addreg-directive.md).

## See also

[DEVPKEY_Device_DeviceDesc](../install/devpkey-device-devicedesc.md)

[INF DDInstall section](../install/inf-ddinstall-section.md)

[DCH Design Principles and Best Practices](../develop/dch-principles-best-practices.md)

[Windows 11 APIs for Audio Processing Objects](windows-11-apis-for-audio-processing-objects.md)