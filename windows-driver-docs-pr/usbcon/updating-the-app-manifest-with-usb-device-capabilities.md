---
Description: This topic describes the device capabilities that are required for a Windows app that uses the Windows.Devices.Usb namespace.
title: How to add USB device capabilities to the app manifest
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to add USB device capabilities to the app manifest


**Summary**

-   You must update Package.appxmanifest with USB device capabilities.
-   The device class must be one of the supported classes.

This topic describes the device capabilities that are required for a Windows app that uses the [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) namespace.

## USB device capability usage


Your USB app must include certain device capabilities in its [App package manifest](https://msdn.microsoft.com/library/windows/apps/br211474) to specify key information about the device. Here are the required elements in hierarchical order:

[**&lt;DeviceCapability&gt;**](https://msdn.microsoft.com/library/windows/apps/br211430): The **Name** attribute must be "usb".

**&lt;Device&gt;**: The **Id** attribute must specify the vendor/product Id or can be "any" to allow access to any device that matches the function type.

**&lt;Function&gt;**: The **Type** attribute can specify the device class code, name, or the device interface GUID.

**Note**  You cannot modify the USB device capability in Microsoft Visual Studio 2013. You must right-click the Package.appxmanifest file in **Solution Explorer** and select **Open With...**, and then **XML (Text) Editor**. The file opens in plain XML.

 

``` syntax
<DeviceCapability Name="usb">
    <Device Id="vidpid:xxxx xxxx">
      <Function Type="classId:xx xx xx"/>
      <Function Type="name:xxxxx"/>
      <Function Type="winUsbId:xxxxx"/>
    </Device>
</DeviceCapability>
```

## Supported USB device classes


-   Names and code values of the supported device classes are as follows:

    -   `name:cdcControl,           classId:02 * *`
    -   `name:physical, classId:05 * *`
    -   `name:personalHealthcare,   classId:0f 00 00`
    -   `name:activeSync,           classId:ef 01 01`
    -   `name:palmSync,             classId:ef 01 02`
    -   `name:deviceFirmwareUpdate, classId:fe 01 01`
    -   `name:irda,                 classId:fe 02 00     `
    -   `name:measurement,          classId:fe 03 *`
    -   `name:vendorSpecific,       classId:ff * *`

    **Note**  Devices that belong to the DeviceFirmwareUpdate class can only be accessed by privileged apps that is explicitly declared by the OEM for that PC.

     

-   Because these are unknown interfaces, the app is required to specify the vendor/product id for these class codes.

    -   CDC (0x02)
    -   CDC-data (0x0A)
    -   Miscellaneous (0xEF)
    -   Application specific (0xFE)
    -   Vendor specific (0xFF)
-   These USB device classes are not supported:

    -   Invalid class (0x00)
    -   Audio class (0x01)
    -   HID class(0x03)
    -   Image class (0x06)
    -   Printer class (0x07)
    -   Mass storage class (0x08)
    -   Smart card class (0x0B)
    -   Audio/video class (0x10)
    -   Wireless controller (such as, wireless USB host/hub) (0xE0)

## USB device capability example


Here are some examples for defining USB device capabilities:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Example</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre class="syntax" space="preserve"><code>&lt;DeviceCapability Name=&quot;usb&quot;&gt;
  &lt;Device Id=&quot;any&quot;&gt;
    &lt;Function Type=&quot;classId:ef 01 01&quot;/&gt;
    &lt;Function Type=&quot;name:stillImage&quot;/&gt;
  &lt;/Device&gt;
&lt;/DeviceCapability&gt;</code></pre></td>
<td><p>Allows the app to access any ActiveSync or StillImage interface on any device. The app is not required to specify the vendor/product identifiers because these are known class types.</p></td>
</tr>
<tr class="even">
<td><pre class="syntax" space="preserve"><code>&lt;DeviceCapability Name=&quot;usb&quot;&gt;
  &lt;Device Id=&quot;vidpid:045e 930a&quot;&gt;
    &lt;Function Type=&quot;name:vendorSpecific&quot;/&gt;
  &lt;/Device&gt;
&lt;/DeviceCapability&gt;</code></pre></td>
<td><p>Allows the app to access a vendor-specific interface on the OSR USB Fx2 device.</p></td>
</tr>
<tr class="odd">
<td><pre class="syntax" space="preserve"><code>&lt;DeviceCapability Name=&quot;usb&quot;&gt;
  &lt;Device Id=&quot;vidpid:045e 930a&quot;&gt;
    &lt;Function Type=&quot;classId:ff * <em>&quot;/&gt;
  &lt;/Device&gt;
&lt;/DeviceCapability&gt;</code></pre></td>
<td><p>Allows the app to access a vendor-specific interface on a different version of the OSR USB Fx2 device. Note the classId format: &quot;ff * *&quot;. The class code is &quot;ff&quot; followed by a wildcard (</em>) to include any subclass and protocol code.</p></td>
</tr>
<tr class="even">
<td><pre class="syntax" space="preserve"><code>&lt;DeviceCapability Name=&quot;usb&quot;&gt;
  &lt;Device Id=&quot; vidpid:1234 5678&quot;&gt;
    &lt;Function Type=&quot;winUsbId:&quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&quot;/&gt;
  &lt;/Device&gt;
&lt;/DeviceCapability&gt;</code></pre></td>
<td><p>Allows the app to access the device with a device interface GUID defined either in the MS OS Descriptor or in the device INF.</p>
<p>In this case, the Device Id value must not equal &quot;any&quot;.</p></td>
</tr>
</tbody>
</table>

 

**App manifest package for the CustomUsbDeviceAccess sample**

``` syntax
  <Capabilities>
      <!--When the device's classId is FF * *, there is a predefined name for the class. You can use the name instead of the class id. 
          There are also other predefined names that correspond to a classId.-->
      <m2:DeviceCapability Name="usb">
          <!--OSRFX2 Device-->
          <m2:Device Id="vidpid:0547 1002">
              <m2:Function Type="classId:ff * *"/>
              <!--<m2:Function Type="name:vendorSpecific"/>-->
          </m2:Device>
          <!--SuperMutt Device-->
          <m2:Device Id="vidpid:045E 0611">
              <!--<m2:Function Type="classId:ff * *"/>-->
              <m2:Function Type="name:vendorSpecific"/>
          </m2b:Device>
      </m2:DeviceCapability>
  </Capabilities>
```

## Related topics
[UWP app for a USB device](writing-usb-device-companion-apps-for-microsoft-store.md)  



