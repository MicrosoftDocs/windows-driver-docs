---
title: PreviousMode
author: windows-driver-content
description: PreviousMode
ms.assetid: 1251cca9-604c-48c0-a136-21dd1fe4fa72
keywords: ["PreviousMode", "RequestorMode"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PreviousMode

유저모드 애플리케이션이 **Nt** 또는 **Zw** 버전의 네이티브 시스템 서비스 루틴을 호출하면 시스템 콜 매커니즘이 호출 스레드를 커널모드로 트랩합니다. 매개 변수 값이 유저모드에서 시작되었음을 알리기 위해 호출자 [thread object](introduction-to-thread-objects.md)의 **PreviousMode** 필드를 **UserMode** 로 설정합니다. 네이티브 시스템 서비스 루틴은 매개변수가 유저모드로부터 왔는지 확인하기 위해 호출 스레드의 **PreviousMode** 필드를 확인합니다.  

만일 커널모드 드라이버가 네이티브 시스템 서비스 루틴을 호출하고 매개 변수를 커널모드 루틴에 전달하는 경우 현재 스레드 오브젝트의 **PreviousMode** 필드는 반드시 **KernelMode** 이어야 합니다. 

커널모드 드라이버는 임의의 스레드 컨텍스트에서 실행 될 수 있고, **PreviousMode** 필드가 **UserMode**로 설정될 수 있습니다. 이 경우 커널모드 드라이버는 **Zw** 버전의 네이티브 서비스 루틴을 호출하여 매개 변수 값이 신뢰할 수 있는, 커널모드 호출임을 알릴 수 있습니다. **Zw** 호출은 현재 스레드 객체의 **PreviousMode** 값을 겹쳐 쓰는 간단한 래퍼함수로 이동합니다. 래퍼함수는 **PreviousMode** 를 **KernelMode**로 설정하고 **Nt** 버전의 루틴을 호출합니다. **Nt** 버전 루틴이 리턴하면 래퍼함수는 스레드 오브젝트의 원래 **PreviousMode** 값으로 복원하고 반환합니다.  

커널모드 드라이버는 **Nt** 버전의 네이티브 시스템 서비스 루틴을 직접 호출할 수 있습니다. 커널모드 드라이버가 유저모드나 커널모드에서 시작될 수 있는 I/O 요청을 처리할때, 드라이버는 **Nt** 버전의 루틴을 호출하여 루틴이 실행되는 동안 현재 스레드의 **PreviousMode** 값이 변경되지 않도록 할 수 있습니다. **Nt*Xxx*** 루틴은 호출 스레드의 **PreviousMode** 값을 통해 매개변수가 유저모드에서 왔는지 커널모드 콤포넌트에서 왔는지 판단하고, 적절하게 처리합니다.  

커널모드 드라이버가 **Nt*Xxx*** 루틴을 호출하고, 현재 스레드 오브젝트의 **PreviousMode** 값이 매개변수의 출처가 유저모드인지, 커널모드인지를 정확하게 가리키지 못한다면 오류가 발생 할 수 있습니다. 

예를 들어, 커널모드 드라이버가 임의의 스레드 컨텍스트에서 실행중이고, **PreviousMode** 값이 **UserMode** 인 경우를 가정합니다. 만일 드라이버가 커널모드 파일 핸들을 [**NtClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417)루틴에 전달한 경우 이 루틴은 **PreviousMode** 값을 확인하고, 핸들이 유저모드 핸들이어야 한다고 결정합니다. **NtClose**가 유저모드 핸들테이블에서 핸들을 찾을 수 없으므로 STATUS\_INVALID\_HANDLE 에러코드를 리턴합니다. 반면에 드라이버는 절대 핸들을 닫을 수 없기 때문에 핸들 누수 상황을 만들게 됩니다. 

다른 예로, 만일 **Nt*Xxx*** 루틴의 매개변수에 입력 또는 출력 버퍼가 포함되어있고, **PreviousMode** = **UserMode** 인 경우 루틴은 버퍼를 검증하기 위해 [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) 또는 [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) 루틴을 호출합니다. 만일 버퍼가 유저모드 메모리가 아니라 시스템 메모리에 할당되어있는 경우 **ProbeFor*Xxx*** 루틴은 예외를 발생시키고, **Nt*Xxx*** 루틴은 STATUS\_ACCESS\_VIOLATION 에러코드를 리턴하게 됩니다. 

필요한 경우 드라이버는 [**ExGetPreviousMode**](https://msdn.microsoft.com/library/windows/hardware/ff545288) 루틴을 호출해서 현재 스레드 오브젝트의 **PreviousMode** 값을 가져올 수 있습니다. 또는 요청된 I/O 작업 정보를 담고있는 [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) 구조체의 **RequestorMode** 필드를 읽을 수 있습니다. **RequestorMode** 필드는 작업을 요청한 스레드의 **PreviousMode** 값의 사본을 포함합니다. 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20PreviousMode%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


