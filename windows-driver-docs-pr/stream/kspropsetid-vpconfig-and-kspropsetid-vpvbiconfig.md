---
title: KSPROPSETID\_VPConfig and KSPROPSETID\_VPVBIConfig
description: KSPROPSETID\_VPConfig and KSPROPSETID\_VPVBIConfig
MS-HAID:
- 'dvdref\_2ab95a14-ec2e-49c0-a15c-477141bd28d6.xml'
- 'stream.kspropsetid\_vpconfig\_and\_kspropsetid\_vpvbiconfig'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3e9a79a2-f217-4736-87b2-a968b358bbc7
---

# KSPROPSETID\_VPConfig and KSPROPSETID\_VPVBIConfig


## <span id="ddk_kspropsetid_vpconfig_and_kspropsetid_vpvbiconfig_ks"></span><span id="DDK_KSPROPSETID_VPCONFIG_AND_KSPROPSETID_VPVBICONFIG_KS"></span>


The KSPROPSETID\_VPConfig and KSPROPSETID\_VPVBIConfig property sets define properties to control video ports (VPs) and the video port vertical blanking interval (VPVBI).

The KSPROPERTY\_VPCONFIG enumeration in *Ksmedia.h* specifies the properties of KSPROPSETID\_VPConfig and KSPROPSETID\_VPVBIConfig.

Minidrivers that use video ports should implement support for the following properties:

[**KSPROPERTY\_VPCONFIG\_NUMCONNECTINFO**](ksproperty-vpconfig-numconnectinfo.md)

[**KSPROPERTY\_VPCONFIG\_GETCONNECTINFO**](ksproperty-vpconfig-getconnectinfo.md)

[**KSPROPERTY\_VPCONFIG\_SETCONNECTINFO**](ksproperty-vpconfig-setconnectinfo.md)

[**KSPROPERTY\_VPCONFIG\_VPDATAINFO**](ksproperty-vpconfig-vpdatainfo.md)

[**KSPROPERTY\_VPCONFIG\_MAXPIXELRATE**](ksproperty-vpconfig-maxpixelrate.md)

[**KSPROPERTY\_VPCONFIG\_NUMVIDEOFORMAT**](ksproperty-vpconfig-numvideoformat.md)

[**KSPROPERTY\_VPCONFIG\_GETVIDEOFORMAT**](ksproperty-vpconfig-getvideoformat.md)

[**KSPROPERTY\_VPCONFIG\_SETVIDEOFORMAT**](ksproperty-vpconfig-setvideoformat.md)

[**KSPROPERTY\_VPCONFIG\_INVERTPOLARITY**](ksproperty-vpconfig-invertpolarity.md)

[**KSPROPERTY\_VPCONFIG\_DECIMATIONCAPABILITY**](ksproperty-vpconfig-decimationcapability.md)

[**KSPROPERTY\_VPCONFIG\_SCALEFACTOR**](ksproperty-vpconfig-scalefactor.md)

[**KSPROPERTY\_VPCONFIG\_DDRAWHANDLE**](ksproperty-vpconfig-ddrawhandle.md)

[**KSPROPERTY\_VPCONFIG\_VIDEOPORTID**](ksproperty-vpconfig-videoportid.md)

[**KSPROPERTY\_VPCONFIG\_DDRAWSURFACEHANDLE**](ksproperty-vpconfig-ddrawsurfacehandle.md)

[**KSPROPERTY\_VPCONFIG\_SURFACEPARAMS**](ksproperty-vpconfig-surfaceparams.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_VPConfig%20and%20KSPROPSETID_VPVBIConfig%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




