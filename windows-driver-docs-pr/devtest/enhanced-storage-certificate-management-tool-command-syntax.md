---
title: Enhanced Storage Certificate Management Tool Command Syntax
description: The Enhanced Storage Certificate Management tool provides certificate management operations by using different command-line switches.
ms.assetid: 4b46bdac-77e3-4b73-8942-64d902d53564
keywords: ["Enhanced Storage Certificate Management Tool Command Syntax Driver Development Tools"]
topic_type:
- apiref
api_name:
- Enhanced
api_type:
- NA
---

# Enhanced Storage Certificate Management Tool Command Syntax


The Enhanced Storage Certificate Management tool provides certificate management operations by using different command-line switches. Each switch defines its own set of parameters, such as volume name and certificate index.

The Enhanced Storage Certificate Management tool is run from the command line.

``` syntax
    EhStorCertMgrCmd 
    [/Add 
    AddParameters 
    |  

    /Clear 
    ClearParameters
    |

    /Debug 
    DebugParameters
    |

    /Export 
    ExportParameters
    |

    /Help|/?|

    /Initialize 
    InitializeParameters

    |
    /List [
    ListParameters
]| 

    /Remove 
    RemoveParameters
    |

    /Replace 
    ReplaceParameters
    ]
   
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________Add______"></span><span id="________add______"></span><span id="________ADD______"></span> **/Add**   
Adds a certificate to the authentication silo certificate (ASC) store on a specified IEEE 1667-compliant USB storage device. For more information, see [**/Add Switch**](enhstor-add-switch.md).

<span id="________Clear______"></span><span id="________clear______"></span><span id="________CLEAR______"></span> **/Clear**   
Removes all certificates from the ASC store on a specified IEEE 1667-compliant USB storage device. For more information, see [**/Clear Switch**](-clear-switch.md).

<span id="________Debug______"></span><span id="________debug______"></span><span id="________DEBUG______"></span> **/Debug**   
Reports on the capabilities and information about the ASC store in an IEEE 1667-compliant USB storage device. For more information, see [**/Debug Switch**](-debug-switch.md).

<span id="________Export______"></span><span id="________export______"></span><span id="________EXPORT______"></span> **/Export**   
Exports a specified certificate from the ASC store in an IEEE 1667-compliant USB storage device to a file. This switch also supports the export of a certificate signing request (CSR) to a file.

For more information, see [**/Export Switch**](-export-switch.md).

<span id="________Help______"></span><span id="________help______"></span><span id="________HELP______"></span> **/Help**   
Displays usage information about the Enhanced Storage Certificate Management tool. The same help information can be displayed by using the **/?** Switch.

<span id="________Initialize______"></span><span id="________initialize______"></span><span id="________INITIALIZE______"></span> **/Initialize**   
Initializes the ASC store in an IEEE 1667-compliant USB storage device to its original manufacturer's state. For more information, see [**/Initialize Switch**](-initialize-switch.md).

<span id="________List______"></span><span id="________list______"></span><span id="________LIST______"></span> **/List**   
Lists all the IEEE 1667-compliant USB storage devices connected to the computer. This switch can also be used to list the certificates within the ASC store in an IEEE 1667-compliant USB storage device.

For more information, see [**/List Switch**](-list-switch.md).

<span id="________Remove______"></span><span id="________remove______"></span><span id="________REMOVE______"></span> **/Remove**   
Removes a specified certificate from the ASC store in an IEEE 1667-compliant USB storage device. For more information, see [**/Remove Switch**](-remove-switch.md).

<span id="________Replace______"></span><span id="________replace______"></span><span id="________REPLACE______"></span> **/Replace**   
Replaces a specified certificate from the ASC store in an IEEE 1667-compliant USB storage device. For more information, see [**/Replace Switch**](-replace-switch.md).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The Enhanced Storage Certificate Management tool cannot add, remove, or replace the ASC-manufacturer (ASCm) certificate from the ASC store in an IEEE 1667-compliant USB storage device. For more information about this and other IEEE 1667 certificate types, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

All the switches of the Enhanced Storage Certificate Management tool must start with either a slash mark ('/') or dash ('-'). The parameters for a switch must begin with a dash character. The switches and the related parameters are case-insensitive.

.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Enhanced%20Storage%20Certificate%20Management%20Tool%20Command%20Syntax%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




