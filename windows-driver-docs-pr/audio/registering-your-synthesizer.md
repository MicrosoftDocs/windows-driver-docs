---
title: Registering Your Synthesizer
description: Registering Your Synthesizer
ms.assetid: c8cb30ba-97ca-49ee-a6ef-2938a0ab780e
keywords:
- DirectMusic custom rendering WDK audio , synthesizers
- custom rendering in user mode WDK audio , synthesizers
- synthesizers WDK audio , registering
- registering synthesizers
- user-mode synths WDK audio , synthesizer registration
- custom synths WDK audio , synthesizer registration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Your Synthesizer


## <span id="registering_your_synthesizer"></span><span id="REGISTERING_YOUR_SYNTHESIZER"></span>


After your software synthesizer is created, it must be added to the system registry so that it is available to applications as a DirectMusic port that can be enumerated. When the installation program calls your DLL's [**DllRegisterServer**](https://msdn.microsoft.com/library/windows/desktop/ms682162) COM function to tell the DLL to register itself as a COM object, the function can register the synthesizer as well. To do so, the function adds an entry to the list of available software synthesizers by creating a key in the following path:

```inf
  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\DirectMusic\SoftwareSynths
```

Header file dmusicc.hdefines constant REGSTR\_PATH\_SOFTWARESYNTHS to represent this path.

The key is named with the class identifier of the synthesizer COM object. Within the key is a string field called "Description" with the name of the synthesizer.

The following example code shows a function, `RegisterSynth`, that can be called from **DllRegisterServer** to register the synthesizer:

```cpp
  const char cszSynthRegRoot[] = REGSTR_PATH_SOFTWARESYNTHS "\\";
  const char cszDescriptionKey[] = "Description";
  const int CLSID_STRING_SIZE = 39;
  HRESULT CLSIDToStr(const CLSID &clsid, char *szStr, int cbStr);
 
  HRESULT RegisterSynth(REFGUID guid,
                        const char szDescription[])
  {
      HKEY hk;
      char szCLSID[CLSID_STRING_SIZE];
      char szRegKey[256];
 
      HRESULT hr = CLSIDToStr(guid, szCLSID, sizeof(szCLSID));
      if (!SUCCEEDED(hr))
      {
          return hr;
      }
 
      strcpy(szRegKey, cszSynthRegRoot);
      strcat(szRegKey, szCLSID);
 
      if (RegCreateKey(HKEY_LOCAL_MACHINE,
                       szRegKey,
                       &hk))
      {
          return E_FAIL;
      }
 
      hr = S_OK;
      if (RegSetValueEx(hk,
                        cszDescriptionKey,
                        0L,
                        REG_SZ,
                        (const unsigned char *)szDescription,
                        strlen(szDescription) + 1))
      {
          hr = E_FAIL;
      }
 
      RegCloseKey(hk);
      return hr;
  }
```

`CLSIDToStr` is a locally defined function (not shown in the preceding code example) that converts a CLSID value to a character string. It is similar to the [**StringFromCLSID**](https://msdn.microsoft.com/library/windows/desktop/ms683917) function that is described in the Microsoft Windows SDK documentation.

 

 




