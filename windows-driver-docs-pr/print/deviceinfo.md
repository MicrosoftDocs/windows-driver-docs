---
title: DeviceInfo
description: DeviceInfo
ms.assetid: be2ee9e7-bd94-4f96-8d93-3b6f5fd9350e
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

```cpp
MANUFACTURER:ACME Manufacturing;
MODEL:LaserBeam 9;
COMMAND SET:PCL,PJL,PS,XHTML-Print+xml;
COMMENT:Anything you like;
ACTIVE COMMAND SET:PCL;
```

 

 




