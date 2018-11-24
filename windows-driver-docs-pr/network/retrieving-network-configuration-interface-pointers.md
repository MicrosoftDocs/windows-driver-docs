---
title: Retrieving Network Configuration Interface Pointers
description: Retrieving Network Configuration Interface Pointers
ms.assetid: ac3638a1-d039-478e-baec-c73d4d1b6751
keywords:
- notify objects WDK networking , interface pointers
- network notify objects WDK , interface pointers
- network configuration interface pointers WDK
- interface pointers WDK networking
- pointers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving Network Configuration Interface Pointers





When the network configuration subsystem initializes an instance of the notify object as described in [Creating and Initializing an Instance of a Notify Object](creating-and-initializing-an-instance-of-a-notify-object.md), the object receives [**INetCfgComponent**](https://msdn.microsoft.com/library/windows/hardware/ff547715) and [**INetCfg**](https://msdn.microsoft.com/library/windows/hardware/ff547694) interface pointers. **INetCfgComponent** points to the notify object's component interface that the object can use to access and control the component. **INetCfg** points to the root network configuration interface that the notify object can use to access all aspects of network configuration. The following code uses these **INetCfgComponent** and **INetCfg** interface pointers to retrieve other network configuration interfaces that the notify object might require.

```C++
// Using the notify object's component interface that the notify 
// object received:
INetCfgComponent *pncfgcompThis, *pncfgcompUp, *pncfgcompLow;
INetCfgComponentBindings *pncfgcompbind;
IEnumNetCfgBindingPath *penumncfgbindpath;
INetCfgBindingPath *pncfgbindpath;
IEnumNetCfgBindingInterface *penumncfgbindintrfc;
INetCfgBindingInterface *pncfgbindintrfc;
HRESULT hr;
DWORD dwFlags;  // EBP_ABOVE or EBP_BELOW
ULONG celt, celtFetched; // Number of requested and returned elements

// Retrieve a pointer to INetCfgComponentBindings to control and 
// retrieve information about bindings for the component.
hr = pncfgcompThis->QueryInterface(IID_INetCfgComponentBindings, 
                                  (LPVOID*)&pncfgcompbind);
// Retrieve a pointer to IEnumNetCfgBindingPath to enumerate binding 
// paths for the component.
hr = pncfgcompbind->EnumBindingPaths(dwFlags, &penumncfgbindpath);
// Retrieve a pointer to INetCfgBindingPath that points to one or more 
// binding paths for the component.
hr = penumncfgbindpath->Next(celt, &pncfgbindpath, &celtFetched);
// Retrieve a pointer to IEnumNetCfgBindingInterface to enumerate 
// the collection of binding interfaces for the binding path.
hr = pncfgbindpath->EnumBindingInterfaces(&penumncfgbindintrfc);
// Retrieve a pointer to INetCfgBindingInterface that points to one or 
// more binding interfaces for the binding path.
hr = penumncfgbindintrfc->Next(celt, &pncfgbindintrfc, &celtFetched);
// Retrieve pointers to INetCfgComponent for network components 
// above and below the binding interface.
hr = pcfgbindintrfc->GetUpperComponent(&pncfgcompUp);
hr = pcfgbindintrfc->GetLowerComponent(&pncfgcompLow);

// Using the root network configuration interface that the notify 
// object received:
INetCfg *pnetcfg;
INetCfgLock *pncfglock;
INetCfgClass *pncfgclass;
INetCfgComponent *pncfgcompOther, *pncfgcompInstall;
INetCfgClassSetup *pncfgclsSetup
GUID *pguidClass; // For example, set to GUID_DEVCLASS_NETTRANS
IEnumNetCfgComponent *penumncfgcomp;
HWND hwndParent; // Handle to Window for selecting.
OBO_TOKEN *pOboToken; // Another component or the user installs.
DWORD dwSetupFlags, dwUpgradeFromBuildNo;
 
// Retrieve a pointer to INetCfgLock to obtain a lock on network 
// configuration.
hr = pnetcfg->QueryInterface(IID_INetCfgLock, (LPVOID*)&pncfglock);
// Retrieve a pointer to INetCfgComponent for a specific component.
hr = pnetcfg->FindComponent(TEXT("MS_TCPIP"), &pncfgcompOther);
// Retrieve a pointer to IEnumNetCfgComponent to enumerate 
// the collection of a particular type of component.
hr = pnetcfg->EnumComponents(pguidClass, &penumncfgcomp);
// Retrieve a pointer to INetCfgClass for a specific class of 
// component.
hr = pnetcfg->QueryNetCfgClass(pguidClass, IID_INetCfgClass, 
                              (LPVOID*)&pncfgclass);
// Retrieve a pointer to INetCfgComponent for a specific component.
hr = pncfgclass->FindComponent(TEXT("MS_TCPIP"), &pncfgcompOther);
// Retrieve a pointer to IEnumNetCfgComponent to enumerate 
// the collection of a particular type of component.
hr = pncfgclass->EnumComponents(&penumncfgcomp);
// Retrieve a pointer to INetCfgComponent that points to one or 
// more components for the particular type of component.
hr = penumncfgcomp->Next(celt, &pncfgcompOther, &celtFetched);
// Retrieve a pointer to INetCfgClassSetup that enables installation 
// or removal of a particular type of component.
hr = pncfgclass->QueryInterface(IID_INetCfgClassSetup, 
                               (LPVOID*)&pncfgclsSetup);
// Retrieve a pointer to INetCfgComponent for an installed component.
hr = pncfgclsSetup->SelectAndInstall(hwndParent, pOboToken,
                                     &pncfgcompInstall);
// Retrieve a pointer to INetCfgComponent for an installed component.
hr = pncfgclsSetup->Install(TEXT("MS_TCPIP"), pOboToken, dwSetupFlags, 
                           dwUpgradeFromBuildNo, TEXT("AnswerFile"), 
                    TEXT("AnswerFileSections"), &pncfgcompInstall);
```

 

 





