---
title: DeviceInfo
description: DeviceInfo
ms.assetid: be2ee9e7-bd94-4f96-8d93-3b6f5fd9350e
---

# DeviceInfo


Schema Path:\\Printer.DeviceInfo

Node Type:Property

The DeviceInfo property contains information about the device as a whole. Much of this data can be set by the user/administrator to personalize the device.

The DeviceInfo property contains the following child values.

FriendlyName

Manufacturer

ModelName

Location

Comment

FirmwareVersion

IEEE1284DeviceID

[NetworkingInfo](networkinginfo.md)

### <span id="friendlyname"></span><span id="FRIENDLYNAME"></span> FriendlyName

Schema Path:\\Printer.DeviceInfo:FriendlyName

Node Type:Value

Data Type:BIDI\_STRING

Description:A user-created, user-settable name that identifies the device.

### <span id="manufacturer"></span><span id="MANUFACTURER"></span> Manufacturer

Schema Path:\\Printer.DeviceInfo:Manufacturer

Node Type:Value

Data Type:BIDI\_STRING

Description:The name of the device manufacturer.

### <span id="modelname"></span><span id="MODELNAME"></span> ModelName

Schema Path:\\Printer.DeviceInfo:ModelName

Node Type:Value

Data Type:BIDI\_STRING

Description:The name of the device model, including the model number, but excluding the manufacturer name.

### <span id="location"></span><span id="LOCATION"></span> Location

Schema Path:\\Printer.DeviceInfo:Location

Node Type:Value

Data Type:BIDI\_STRING

Description:The current location of the device.

### <span id="comment"></span><span id="COMMENT"></span> Comment

Schema Path:\\Printer.DeviceInfo:Comment

Node Type:Value

Data Type:BIDI\_STRING

Description:A string containing information important to the administrator or organization in which the device resides.

### <span id="firmwareversion"></span><span id="FIRMWAREVERSION"></span> FirmwareVersion

Schema Path:\\Printer.DeviceInfo:FirmwareVersion

Node Type:Value

Data Type:BIDI\_STRING

Description:A string that contains the current firmware version of the device.

### <span id="ieee1284deviceid"></span><span id="IEEE1284DEVICEID"></span> IEEE1284DeviceID

Schema Path:\\Printer.DeviceInfo:IEEE1284DeviceID

Node Type:Value

Data Type:BIDI\_STRING

Description:A string that contains the IEEE 1284-2000 device ID for the device. Note that the length field must not be specified. The value is assigned by the Printer vendor and must not be localized by the Print Service.

The IEEE 1284-2000 device ID is a length field followed by a case-sensitive string of ASCII characters that define peripheral characteristics and capabilities. The length bytes must not be included. The device ID sequence is composed of a series of keys and values of the form:

key: value {,value}, repeated for each key

As indicated, each key will have one value and might have more than one value. The minimum necessary keys (case-sensitive) are MANUFACTURER and MODEL. (These keys might be abbreviated as MFG and MDL respectively.) Each implementation must supply these two keys, and possibly additional ones. Each key (and each value) is a string of characters. Any characters except colon (:), comma (,), and semi-colon (;) can be included as part of the key (or value) string. Any leading or trailing white space (SPACE\[x'20'\], TAB\[x'09'\], VTAB\[x'0B'\], CR\[x'0D'\], NL\[x'0A'\], or FF\[x'0C'\]) in the string is ignored by the parsing program (but is still counted as part of the overall length of the sequence).

The following code example shows an ID string, which shows the optional command set, comment, and active command set keys and their associated values.

**Note**   All of the text must be on one line.

 

```
MANUFACTURER:ACME Manufacturing;
MODEL:LaserBeam 9;
COMMAND SET:PCL,PJL,PS,XHTML-Print+xml;
COMMENT:Anything you like;
ACTIVE COMMAND SET:PCL;
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DeviceInfo%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




