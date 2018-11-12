---
title: MSFC\_FibrePortHBAMethods WMI Class
description: MSFC\_FibrePortHBAMethods WMI Class
ms.assetid: 7c9f5c94-0c50-4a7a-b05e-41e93409d1e3
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_FibrePortHBAMethods WMI Class


## <span id="ddk_msfc_fibreporthbamethods_wmi_class_kr"></span><span id="DDK_MSFC_FIBREPORTHBAMETHODS_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_FibrePortHBAMethods class to expose operations that can be performed on a Fibre Channel port. This class defines just one method, **ResetStatistics**:

```cpp
class MSFC_FibrePortHBAMethods
{
    [key] 
    string InstanceName;
    boolean Active;
    [ Implemented, WmiMethodId(1)]
    void ResetStatistics();
};
```

The **ResetStatistics** method requires no input or output buffers. The miniport driver should do whatever is required in this method to reset port statistics. There should be one instance of this class for each port.

 

 





