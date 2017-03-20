---
Description: The WpdHelloWorldDriver Sample
MS-HAID: 'wpddk.the\_sample\_driver\_architecture'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: The WpdHelloWorldDriver Sample
---

# The WpdHelloWorldDriver Sample


The sample driver supports four objects: a device object, a storage object, a folder object, and a file object. Each object supports corresponding properties. These properties are defined in the file *WpdObjectProperties.h*.

The sample driver supports a device object that exposes ten read-only properties. These properties, their types, and their values are listed in the following table.

| Property name                     | Property type | Value                              |
|-----------------------------------|---------------|------------------------------------|
| DEVICE\_PROTOCOL                  | String        | "Hello World Protocol ver 1.00"    |
| DEVICE\_FIRMWARE\_VERSION         | String        | "1.0.0.0"                          |
| DEVICE\_POWER\_LEVEL              | Integer       | 100                                |
| DEVICE\_MODEL                     | String        | "Hello World!"                     |
| DEVICE\_MANUFACTURER              | String        | "Windows Portable Devices Group"   |
| DEVICE\_FRIENDLY                  | String        | "Hello World!"                     |
| DEVICE\_SERIAL\_NUMBER            | String        | "01234567890123-45676890123456"    |
| DEVICE\_SUPPORTS\_NONCONSUMABLE   | Bool          | True                               |
| WPD\_DEVICE\_TYPE                 | Integer       | WPD\_DEVICE\_TYPE\_GENERIC         |
| WPD\_FUNCTIONAL\_OBJECT\_CATEGORY | GUID          | WPD\_FUNCTIONAL\_CATEGORY\_STORAGE |

 

The driver supports a storage object that exposes six read-only properties. These properties, their types, and their values are listed in the following table.

| Property name                     | Property type  | Value                              |
|-----------------------------------|----------------|------------------------------------|
| STORAGE\_CAPACITY                 | 64-bit Integer | 1024 \* 1024                       |
| STORAGE\_FREE\_SPACE\_IN\_BYTES   | 64-bit Integer | (same as above)                    |
| STORAGE\_SERIAL\_NUMBER           | String         | 98765432109876-54321098765432      |
| STORAGE\_FILE\_SYSTEM\_TYPE       | String         | FAT32                              |
| STORAGE\_DESCRIPTION              | String         | Hello World! Memory Storage System |
| WPD\_STORAGE\_TYPE                | Integer        | WPD\_STORAGE\_TYPE\_FIXED\_ROM     |
| WPD\_FUNCTIONAL\_OBJECT\_CATEGORY | GUID           | WPD\_FUNCTIONAL\_CATEGORY\_STORAGE |

 

The driver supports a folder object that exposes three read-only properties. These properties, their types, and their values are listed in the following table.

| Property name                            | Property type | Value              |
|------------------------------------------|---------------|--------------------|
| WPD\_OBJECT\_DATE\_MODIFIED              | Date          | 2006/6/26 5:0:0.0  |
| WPD\_OBJECT\_DATE\_CREATED               | Date          | 2006/1/25 12:0:0.0 |
| WPD\_OBJECT\_ORIGINAL\_FILE\_NAME\_VALUE | String        | Documents          |

 

The driver supports a file object that exposes three read-only properties. These properties, their types, and their values are listed in the following table.

| Property name                     | Property type | Value              |
|-----------------------------------|---------------|--------------------|
| WPD\_OBJECT\_DATE\_MODIFIED       | Date          | 2006/6/26 5:0:0.0  |
| WPD\_OBJECT\_DATE\_CREATED        | Date          | 2006/1/25 12:0:0.0 |
| WPD\_OBJECT\_ORIGINAL\_FILE\_NAME | String        | Readme.txt         |

 

In addition to the above properties, every object (for example, device, storage, folder, or file) also supports seven common WPD object properties. These are read-only properties that contain object-specific values for the most part. These properties, their types, and their values are listed in the following table.

|                                     |               |                 |
|-------------------------------------|---------------|-----------------|
| Property name                       | Property type | Value           |
| WPD\_OBJECT\_ID                     | String        | Object-specific |
| WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID | String        | Object-specific |
| WPD\_OBJECT\_PARENT\_ID             | String        | Object-specific |
| WPD\_OBJECT\_NAME                   | String        | Object-specific |
| WPD\_OBJECT\_FORMAT                 | GUID          | Object-specific |
| WPD\_OBJECT\_CONTENT\_TYPE          | GUID          | Object-specific |
| WPD\_OBJECT\_CAN\_DELETE            | Bool          | False           |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20WpdHelloWorldDriver%20Sample%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



