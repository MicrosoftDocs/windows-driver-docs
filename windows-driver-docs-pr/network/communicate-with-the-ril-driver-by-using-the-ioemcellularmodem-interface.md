---
title: Communicate with the RIL driver by using the IOemCellularModem interface
description: This topic provides information on how to communicate with the RIL driver by using the IOemCellularModem interface.
keywords:
- Communicate with the RIL driver by using the IOemCellularModem interface network drivers
ms.date: 11/07/2017
---

# Communicate with the RIL driver by using the IOemCellularModem interface

> [!WARNING]
> The Cellular COM API is deprecated in Windows 10. This content is provided to support maintenance of OEM and mobile operator created Windows Phone 8.1 applications.

You can use the [IOemCellularModem](/previous-versions/windows/hardware/cellular/dn946687(v=vs.85)) interface to communicate with OEM RIL driver. This is a case where partners can use APIs in the restricted platform allow list (RPAL) to communicate with the modem.

For more information about the cellular COM APIs, see [Cellular COM API reference](/previous-versions/windows/hardware/cellular/dn946508(v=vs.85)).

## Using cellular COM APIs

To use the cellular COM APIs, get a pointer to an [IOemCellular](/previous-versions/windows/hardware/cellular/dn946677(v=vs.85)) instance by calling **CoCreateInstanceFromApp**. The calling application needs this pointer to IOemCellular interface in order to use the [IOemCellularModem](/previous-versions/windows/hardware/cellular/dn946687(v=vs.85)) interface. 

The [IOemCellular::RegisterForOemModemExistenceChanges](/previous-versions/windows/hardware/cellular/dn931023(v=vs.85)) method can be used to list the modems. After the method is called, [IOemCellularModemExistenceChange::OnOemModemAdded](/previous-versions/windows/hardware/cellular/dn946689(v=vs.85)) is invoked with the [IOemCellularModem](/previous-versions/windows/hardware/cellular/dn946687(v=vs.85)) pointer.

This code shows retrieving the [IOemCellular](/previous-versions/windows/hardware/cellular/dn946677(v=vs.85)) pointer by using **CoCreateInstanceFromApp**. CoCreateInstanceFromApp can return one or more pointers to specific interfaces. The desired interface is IOemCellular, which is specified by query[0].pIID. OemCellular is a reference to the supporting COM class; it determines the factory that activates the class. 

```c++
    MULTI_QI query[1];
    query[0].pIID = &__uuidof(IOemCellular);
    query[0].pItf = nullptr;
    query[0].hr = S_OK;

    hr = CoCreateInstanceFromApp(__uuidof(OemCellular), nullptr, CLSCTX_INPROC_SERVER,
                                nullptr, _countof(query), query);
    ...
```
This code shows registering a pointer to [IOemCellularModemExistenceChange](/previous-versions/windows/hardware/cellular/dn946688(v=vs.85)) by using [IOemCellular::RegisterForOemModemExistenceChanges](/previous-versions/windows/hardware/cellular/dn931023(v=vs.85)). In the code below, this is a pointer to **CModems** which provides the IOemCellularModemExistenceChange interface.

```c++
    HRESULT hr;
    hr = m_spCellular->RegisterForOemModemExistenceChanges(this);

    ...
```

This code shows how to implement **OnOemModemAdded** and the other methods for the [IOemCellularModemExistenceChange](/previous-versions/windows/hardware/cellular/dn946688(v=vs.85)) interface.

```c++
class CModems : public IOemCellularModemExistenceChange, public CellBase
{
    ...

    // 
    // IOemCellularModemExistenceChange interface
    //
    IFACEMETHOD(OnOemModemAdded)(IOemCellularModem *pModem);
    IFACEMETHOD(OnOemModemRemoved)(IOemCellularModem *pModem);
    IFACEMETHOD(OnOemModemExistenceDone)();

    ...
};
IFACEMETHODIMP CModems::OnOemModemAdded(IOemCellularModem *pModem)
{
    ComPtr<IOemCellularModem> spModem(pModem);
    m_ModemList.push_back(spModem);
    return S_OK;
}
```

## Sending opaque data to RIL

After you receive an **IOemCellularModem** pointer by invoking **OnOemModemAdded**, [IOemCellularModem::SendModemOpaqueCommand](/previous-versions/windows/hardware/cellular/dn931017(v=vs.85)) can be used. Behind the scenes, cellcore calls the **RIL_DevSpecific** function with the passed parameters. The RIL driver handles this request and sends the response back to the upper layers. After the response is delivered, a callback to [IModemOpaqueCommandCompletion::OnModemOpaqueCommandCompletion](/previous-versions/windows/hardware/cellular/dn946648(v=vs.85)) is invoked with the result of the **SendModemOpaqueCommand** call.

This code shows sending opaque data with the [IOemCellularModem::SendModemOpaqueCommand](/previous-versions/windows/hardware/cellular/dn931017(v=vs.85)).

```c++
    void CCellcoreComponent::CAgent::SetRadioPowerState(bool fPowerOn)
    {
        DWORD command[2];
        command[0] = CMD_SET_EQUIPMENTSTATE;
        command[1] = fPowerOn ? RIL_EQSTATE_FULL : RIL_EQSTATE_MINIMUM;
        m_spModem->SendModemOpaqueCommand(this, (BYTE*)command, sizeof(command), 
            (INT_PTR) CMD_SET_EQUIPMENTSTATE);
    ...
```

In the previous code example, a command is sent to RIL in order to turn the radio on or off. The RIL driver should be designed to handle the two DWORD data elements when **RIL_DevSpecific** is called. You can define your own structure and commands to suit your needs. After completion of a command, the RIL driver sends the response and then a completion callback ([IModemOpaqueCommandCompletion::OnModemOpaqueCommandCompletion](/previous-versions/windows/hardware/cellular/dn946648(v=vs.85))) is invoked. 

This code shows handling the receiving completion event for the **SendModemOpaqueCommand** command in the previous example.

```c++
IFACEMETHODIMP CCellcoreComponent::CAgent::OnModemOpaqueCommandCompletion (
            /* [in] */ HRESULT result,
            /* [size_is][in] */ BYTE *pOpaqueResponse,
            /* [in] */ DWORD cbSize,
            /* [in] */ INT_PTR context)
{
    if (SUCCEEDED(result))
    {
        if ((int)context == CMD_SET_EQUIPMENTSTATE)
        {
            //
            // add routine if it is necessary to handle completion.
            //
        }
    }

    return S_OK;
}
```

> [!NOTE]
> **Maximum request, response and notification size** - The RIL Adaptation Layer imposes a maximum size constraint of 0x2800 (10240) bytes for the RIL command, response, and notification payloads. A payload larger then this size, will generate a fatal error.

## Receiving a notification from RIL

The cellular interface provides a number of RIL notifications that begin with **RIL_NOTIFY**, like **RIL_NOTIFY_SIGNALQUALITY**. But **IOemCellularModem** doesn’t provide a default method to receive these RIL notifications. One option is to use [IOemCellularModem::RegisterForOpaqueModemNotifications](/previous-versions/windows/hardware/cellular/dn931015(v=vs.85)) for these OEM RIL notifications. To do this, first define your own RIL notification message that is less than **RIL_NOTIFY_OEM_MAX**, which is defined in RilAPITypes.h. Whenever RIL sends an OEM RIL notification, [IOpaqueModemNotifications::OnOpaqueModemNotifications](/previous-versions/windows/hardware/cellular/dn931072(v=vs.85)) is called after a callback pointer is registered by IOemCellularModem::RegisterForOpaqueModemNotifications. 

This code shows how to call [IOemCellularModem::RegisterForOpaqueModemNotifications](/previous-versions/windows/hardware/cellular/dn931015(v=vs.85)).

```c++
HRESULT CCellcoreComponent::CAgent::Initialize()
{
    ...
    IFFAILED_EXIT(m_spModem->RegisterForOpaqueModemNotifications(this));
    ...
```

This code shows how to implement [IOpaqueModemNotifications::OnOpaqueModemNotifications](/previous-versions/windows/hardware/cellular/dn931072(v=vs.85)). The code contains a notification callback handle that returns the number of signal bars. The custom-defined notification RIL_NOTIFY_OEM_SIGNALSTRENGTH should be implemented in both the calling application and in the RIL driver.

```c++
class CAgent : 
        public IOpaqueModemNotifications, 
        public IModemOpaqueCommandCompletion,
        public IPowerStateChange,
        public IPositionInfoCompletion,
        public IAgent
{
    ...

    //
    // IOpaqueModemNotifications
    //
    IFACEMETHOD(OnOpaqueModemNotifications)( 
    /* [in] */ DWORD dwCode,
    /* [in] */ BYTE *pOpaqueNotification,
    /* [in] */ DWORD cbSize);

                }
IFACEMETHODIMP CCellcoreComponent::CAgent::OnOpaqueModemNotifications( 
            /* [in] */ DWORD dwCode,
            /* [in] */ BYTE *pOpaqueNotification,
            /* [in] */ DWORD cbSize)
{
    wchar_t szResultString[STRING_BUF_LEN] = {0,};

    // check dwCode to fill notification result string.
    if (dwCode == RIL_NOTIFY_OEM_SIGNALSTRENGTH)
    {
        DWORD dwSignalBar;
        if (cbSize == sizeof(DWORD))
        {
            dwSignalBar = *((DWORD*)pOpaqueNotification);
        }
        else
        {
            dwSignalBar = -1;
        }

        swprintf_s(szResultString, STRING_BUF_LEN, L"Num of signal bars : %d", dwSignalBar );
    }
    else
    {
        swprintf_s(szResultString, STRING_BUF_LEN, L"Unknown Notification");
    }

    // send notification string.
    String ^ opaqueInfo = ref new String (szResultString);
    m_cellcore->OnOpaqueNotification(opaqueInfo);

    return S_OK;
}
```

## Related topics

[Cellular COM API design guide](cellular-com-api-design-guide.md)

[Cellular COM API reference](/previous-versions/windows/hardware/cellular/dn946508(v=vs.85))
