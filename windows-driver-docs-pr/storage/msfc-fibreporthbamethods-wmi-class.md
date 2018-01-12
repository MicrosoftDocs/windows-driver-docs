---
title: MSFC\_FibrePortHBAMethods WMI Class
description: MSFC\_FibrePortHBAMethods WMI Class
ms.assetid: 7c9f5c94-0c50-4a7a-b05e-41e93409d1e3
---

# MSFC\_FibrePortHBAMethods WMI Class


## <span id="ddk_msfc_fibreporthbamethods_wmi_class_kr"></span><span id="DDK_MSFC_FIBREPORTHBAMETHODS_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_FibrePortHBAMethods class to expose operations that can be performed on a Fibre Channel port. This class defines just one method, **ResetStatistics**:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_FibrePortHBAMethods%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




