---
title: Adding a Component
description: Adding a Component
ms.assetid: f8177904-77a2-4d1a-8c72-0b47a100bc37
keywords:
- notify objects WDK networking , adding components
- network notify objects WDK , adding components
- adding network components
- network component additions WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding a Component





The network configuration subsystem can inform a notify object when the subsystem adds network components. After initializing a notify object, the subsystem calls the notify object's [**INetCfgComponentNotifyGlobal::GetSupportedNotifications**](https://msdn.microsoft.com/library/windows/hardware/ff547734) method to retrieve the types of notifications required by the object. If the notify object specified that it required notification when network components are added, the subsystem calls the notify object's [**INetCfgComponentNotifyGlobal::SysNotifyComponent**](https://msdn.microsoft.com/library/windows/hardware/ff547736) method and passes NCN\_ADD to inform the notify object that the subsystem installed a network component. If the component that owns the notify object should bind to the specified component, the notify object should perform operations to facilitate the binding. For example, the following code shows how the notify object can bind its component to the specified component if the specified component is a required physical network card.

```cpp
HRESULT CSample::SysNotifyComponent(DWORD dwChangeFlag,
        INetCfgComponent* pnccItem)
{
    HRESULT hr = S_OK;
    INetCfgComponentBindings *pncfgcompbind;
    // Retrieve bindings for the notify object&#39;s component (m_pncc)
    hr = m_pncc->QueryInterface(IID_INetCfgComponentBindings, 
                                (LPVOID*)&pncfgcompbind);
    // Determine if notification is about adding a component
    if (SUCCEEDED(hr) && (NCN_ADD & dwChangeFlag)) {
        // Retrieve the characteristics of the added component
        DWORD dwcc;
        hr = pnccItem->GetCharacteristics(&dwcc);
        // Determine if the added component is a physical adapter
        if (SUCCEEDED(hr) && (dwcc & NCF_PHYSICAL)) {
            // Determine the component&#39;s ID
            LPWSTR pszwInfId;
            hr = pnccItem->GetId(&pszwInfId);
            if (SUCCEEDED(hr)) {
                // Compare the component&#39;s ID to the required ID
                // and if they are the same perform the binding.
                static const TCHAR c_szCompId[] = TEXT("BINDTO_NIC");
                if (!_tcsicmp(pszwInfId, c_szCompId)) {
                    hr = pncfgcompbind->BindTo(pnccItem);
                }
            }
        }
    }
    return hr;
}
```

 

 





