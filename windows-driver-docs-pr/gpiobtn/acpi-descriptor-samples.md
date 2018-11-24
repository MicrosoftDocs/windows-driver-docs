---
title: ACPI descriptor samples
description: This topic contains ACPI descriptor samples.
ms.assetid: E091DF59-2E9F-4652-801C-3F55CBB910FE
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ACPI descriptor samples


This topic contains ACPI descriptor samples.

**Note**  Use only 4 chars length for ACPI descriptors for device definitions (such as CONV).

 

## <span id="ACPI_description_for_button_array"></span><span id="acpi_description_for_button_array"></span><span id="ACPI_DESCRIPTION_FOR_BUTTON_ARRAY"></span>ACPI description for button array


``` syntax
Device(BTT00N)
{
    Method(_HID, 0x0, NotSerialized)
    {
        Return("ID9000")
    }
        Name(_CID, "PNP0C40")
        Name(_CRS, ResourceTemplate()
                {
                GpioInt(Edge, 
                        ActiveLow, 
                        SharedAndWake, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                 {0xE1}
                GpioInt(Edge, 
                        ActiveBoth, 
                        SharedAndWake, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                {0xE2}
                GpioInt(Edge, 
                        ActiveBoth, 
                        Exclusive, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                {0xE3}
                GpioInt(Edge, 
                        ActiveBoth, 
                        Exclusive, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                {0xE4}
                GpioInt(Edge, 
                        ActiveBoth, 
                        Exclusive, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                {0xE5}
                })
}
```

## <span id="ACPI_description_for_laptop_slate_mode_indicator"></span><span id="acpi_description_for_laptop_slate_mode_indicator"></span><span id="ACPI_DESCRIPTION_FOR_LAPTOP_SLATE_MODE_INDICATOR"></span>ACPI description for laptop/slate mode indicator


``` syntax
Device(CONV)
{
    Method(_HID, 0x0, NotSerialized)
        {
            Return("ID9001")
        }
     Name(_CID, "PNP0C60")
}
```

## <span id="ACPI_description_for_docking_mode_indicator"></span><span id="acpi_description_for_docking_mode_indicator"></span><span id="ACPI_DESCRIPTION_FOR_DOCKING_MODE_INDICATOR"></span>ACPI description for docking mode indicator


``` syntax
Device(DOCK)
{
    Method(_HID, 0x0, NotSerialized)
    {
        Return("ID9002")
     }
     Name(_CID, "PNP0C70")
}
```

 

 




