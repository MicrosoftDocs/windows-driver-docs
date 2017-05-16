---
title: Sample PowerShell script to query SMBIOS locally
description: Sample PowerShell script to query SMBIOS locally
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Sample PowerShell script to query SMBIOS locally


List of ChassisTypes copied from DMTF\\SBIOS latest specification document

```
# Set-ExecutionPolicy or Script Signing documentation needs to be reviewed
# Current script is designed to run on individual machines
#

#
$ChassisTypes =
@{
    1='Other'
    2='Unknown'
    3='Desktop'
    4='Low Profile Desktop'
    5='Pizza Box'
    6='Mini Tower'
    7='Tower'
    8='Portable'
    9='Laptop'
    10='Notebook'
    11='Hand Held'
    12='Docking Station'
    13='All in One'
    14='Sub Notebook'
    15='Space-Saving'
    16='Lunch Box'
    17='Main System Chassis'
    18='Expansion Chassis'
    19='SubChassis'
    20='Bus Expansion Chassis'
    21='Peripheral Chassis'
    22='Storage Chassis'
    23='Rack Mount Chassis'
    24='Sealed-Case PC'
    25='Multi-system chassis'
    26='Compact PCI'
    27='Advanced TCA'
    28='Blade'
    29='Blade Enclosure'
    30='Tablet'
    31='Convertible'
    32='Detachable'
    33='IoT Gateway'
    34='Embedded PC'
    35='Mini PC'
    36='Stick PC'
}

$namespace = "root\CIMV2"

$machines = New-Object System.Collections.ArrayList

# TODO: add code to populate the machine list from user input, etc.
#
$machines. Add("LocalHost") | Out-Null

$list = New-Object System.Collections.ArrayList

foreach ($machine in $machines)
{
    $obj = New-Object -Type PSObject | Select-Object SerialNumber, Manufacturer, UUID, BaseBoardProduct, ChassisTypes, Chassis, SystemFamily, SystemSKUNumber

    $obj.SerialNumber = Get-WmiObject -class Win32_Bios -computername $machine -namespace $namespace | Select-Object -ExpandProperty SerialNumber
    $obj.Manufacturer = Get-WmiObject -class Win32_Bios -computername $machine -namespace $namespace | Select-Object -ExpandProperty Manufacturer
    $obj.UUID = Get-WmiObject Win32_ComputerSystemProduct | Select-Object -ExpandProperty UUID
    $obj.BaseBoardProduct = Get-WmiObject Win32_BaseBoard | Select-Object -ExpandProperty Product
    $obj.ChassisTypes = Get-WmiObject Win32_SystemEnclosure | Select-Object -ExpandProperty ChassisType
    $obj.Chassis = $ChassisTypes[[int]$obj.ChassisTypes]
    $obj.SystemFamily = Get-WmiObject Win32_ComputerSystem | Select-Object -ExpandProperty SystemFamily
    $obj.SystemSKUNumber = Get-WmiObject Win32_ComputerSystem | Select-Object -ExpandProperty SystemSKUNumber

    $list.Add($obj) | Out-Null
}

# TODO: add code to handle output (save to local file, upload to share, etc.)
#
# to use on single line for each object
# $list | Sort-Object Manufacturer, Chassis | Format-Table Manufacturer, ChassisTypes, Chassis, SystemFamily, BaseBoard_Product, SerialNumber, UUID, SystemSKUNumber -Wrap

# Optional: pipe to Excel:
# $list | Export-Csv c:\path\filename.csv -Encoding Unicode -NoTypeInformation
#
# Optional: pipe to UI
# $list | Out-GridView
#
$list
```

Sample output:

![Sample output](images/sample-output.png)

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


