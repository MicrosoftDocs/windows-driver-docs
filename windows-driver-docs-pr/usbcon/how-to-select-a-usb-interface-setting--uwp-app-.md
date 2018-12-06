---
Description: Use the UsbInterfaceSetting object to get the current setting and set a setting in the interface.
title: How to select a USB interface setting (UWP app)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to select a USB interface setting (UWP app)


**Summary**

-   How to get the current USB interface setting
-   How to select a USB setting

**Important APIs**

-   [**UsbInterfaceSetting.Selected**](https://msdn.microsoft.com/library/windows/apps/dn264285)
-   [**UsbInterfaceSetting.SelectSettingAsync**](https://msdn.microsoft.com/library/windows/apps/dn264286)

In this topic, you'll learn about changing a setting within a USB interface. You'll use the [**UsbInterfaceSetting**](https://msdn.microsoft.com/library/windows/apps/dn264278) object to get the current setting and set a setting in the interface.

## Before you start...


-   You must have opened the device and obtained the [**UsbDevice**](https://msdn.microsoft.com/library/windows/apps/dn263883) object. Read [How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md).
-   Code examples are based on the CustomUSBDevice sample. You can download the complete sample from this code gallery page.
-   

## About USB interface settings


Each USB interface exposes one or more endpoints that are grouped in *interface settings*. Those settings are device-defined and identified with a number called the *setting index*. Each interface must have *only one* active setting. For a multiple interface device, each interface must have an active setting. If a setting is active, data can be transferred to or from its endpoints. Endpoints in non-active settings are disabled for data transfers.

A setting is said to be active after it has been selected on the device. The default active setting is the first setting of an interface.

Each setting is represented by a [**UsbInterfaceSetting**](https://msdn.microsoft.com/library/windows/apps/dn264278) object. By using the object, your UWP app can perform these operations:

-   Determine whether a particular setting is active while enumerating all settings in an interface.
-   Initiate a request that selects an setting.

For information about USB interface settings, see [USB device layout](usb-device-layout.md).
## Get the active setting of a USB interface


1.  Get the [**UsbInterface**](https://msdn.microsoft.com/library/windows/apps/dn264121) object from the previous obtained [**UsbDevice**](https://msdn.microsoft.com/library/windows/apps/dn263883) object. This code example gets the first interface in the USB configuration. For a multiple-interface device, you can get the **UsbInterface** object that you want to use by enumerating all interfaces. You can get that array through the [**UsbConfiguration.UsbInterfaces**](https://msdn.microsoft.com/library/windows/apps/dn263808) property value.
2.  Get all settings defined in the interface as an array of [**UsbInterfaceSetting**](https://msdn.microsoft.com/library/windows/apps/dn264278) objects by getting the [**UsbInterface.InterfaceSettings**](https://msdn.microsoft.com/library/windows/apps/dn264291) property value.
3.  Enumerate the array and in each iteration check whether the setting is active by checking the [**UsbInterfaceSetting.Selected**](https://msdn.microsoft.com/library/windows/apps/dn264285) property.

This example code shows how to get the setting number for all settings defined in the default interface.

```CSharp
void GetInterfaceSetting (UsbDevice device)
{
        auto interfaceSettings = device.InterfaceSettings;

        for each(UsbInterfaceSetting interfaceSetting in interfaceSettings)
        {
            if (interfaceSetting->Selected)
            {
                uint8 interfaceSettingNumber = interfaceSetting.InterfaceDescriptor.AlternateSettingNumber;

                // Use the interface setting number. Not shown.

                break;
            }
        }
}
```

## Set a USB interface setting


To select a setting that is not currently active, you must find the [**UsbInterfaceSetting**](https://msdn.microsoft.com/library/windows/apps/dn264278) object for the setting to select and then start an asynchronous operation by calling the [**UsbInterfaceSetting.SelectSettingAsync**](https://msdn.microsoft.com/library/windows/apps/dn264286) method. The operation does not return a value.

```CSharp
private async void SetInterfaceSetting(UsbDevice device, Byte settingNumber)
{
    var interfaceSetting = device.DefaultInterface.InterfaceSettings[settingNumber];

    await interfaceSetting.SelectSettingAsync();

    MainPage.Current.NotifyUser("Interface Setting is set to " + settingNumber, NotifyType.StatusMessage);
}
```








