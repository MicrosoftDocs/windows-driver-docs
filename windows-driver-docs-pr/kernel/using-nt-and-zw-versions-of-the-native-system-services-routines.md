---
title: Using Nt and Zw Versions of the Native System Services Routines
author: windows-driver-content
description: Using Nt and Zw Versions of the Native System Services Routines
ms.assetid: 89627ddb-621d-4d27-acd6-16308689165d
keywords: ["Native System Services API WDK"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Nt and Zw Versions of the Native System Services Routines

Windows 의 네이티브 서비스 API 는 커널모드에서 동작하는 루틴들의 집합으로 이루어져있습니다. 이 루틴들의 이름은 **Nt** 또는 **Zw** 로 시작합니다. 커널모드 드라이버들은 이 루틴들을 직접 호출할 수 있으며, 유저모드 어플리케이션들은 시스템 콜을 통해서 이 루틴들을 호출할 수 있습니다.  

몇몇 예외사항이 있긴 하지만 각각의 네이티브 시스템 서비스 루틴들은 비슷한 이름의 접두어만 다른 두가지 버전이 있습니다. 예를 들어 [NtCreateFile](http://go.microsoft.com/fwlink/p/?linkid=157250) 와 [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424) 호출은 비슷한 작업을 수행하지만 사실은 동일한 커널모드 시스템 루틴에 의해서 처리됩니다. 유저모드에서의 **Nt** 와 **Zw** 버전 루틴은 동일하지만 커널모드에서의 **Nt** 와 **Zw** 버전 루틴들은 호출자가 전달한 파라미터 값을 다루는 방식이 다릅니다. 

커널모드 드라이버는 전달되는 매개변수가 신뢰 할 수 있는 커널모드에서 전달된 것임을 알리기 위해 **Zw** 버전의 네이티브 서비스 루틴을 호출합니다. 이 경우 루틴은 매개변수를 검증하지 않고 안전하게 사용할 수 있다고 가정합니다. 그러나 매개변수가 유저모드 또는 커널모드 중 하나일 경우라면 드라이버는 **Nt** 버전의 루틴을 호출하는데 이는 루틴을 호출한 스레드의 기록을 기반으로 매개변수가 유저모드에서 전달되었는지 커널모드에서 전달되었는지를 구별합니다. 커널모드 매개변수와 유저모드 매개변수를 구분하는 방법에 대한 자세한 내용은 [**PreviousMode**](previousmode.md)를 참조하십시오.

유저모드 애플리케이션이 **Nt** 또는 **Zw** 버전의 네이티브 시스템 서비스 루틴을 호출하면 루틴은 항상 매개변수는 신뢰할 수 없는 유저모드에서 전달된 것으로 간주하고 매개변수를 사용하기 전에 철저히 검증합니다. 특히 루틴은 호출자가 제공한 버퍼를 검사하여 버퍼가 유효한 유저모드 메모리에 존재하고 있으며 올바르게 정렬되어있는지 확인합니다.

네이티브 시스템 서비스 루틴은 매개변수에 대한 추가적인 가정을 합니다. 만일 커널모드 드라이버가 할당한 버퍼의 포인터를 매개변수로 받은 경우 버퍼는 유저모드 메모리가 아니라 시스템 메모리에 할당되어있다고 가정합니다. 만일 유저모드 애플리케이션에서 열어둔 핸들을 받으면 루틴은 커널모드 핸들테이블이 아니라 유저모드 핸들테이블에서 핸들을 찾습니다.  

몇 가지 예에서 매개변수 값의 의미는 사용자 모드 및 커널모드에서의 호출간에 더 크게 다릅니다. 예를 들어 [**ZwNotifyChangeKey**](https://msdn.microsoft.com/library/windows/hardware/ff566488) 루틴 (또는 해당 **NtNotifyChangeKey** 버전)에는 입력 매개변수 쌍이 있습니다. *ApcRoutine* 과 *ApcContext* 는 유저모드에서의 호출인지 커널모드에서의 호출인지에 따라 의미가 다릅니다. 유저모드 호출인 경우 *ApcRoutine*은 APC 루틴을 가리키고, *ApcContext*는 APC 루틴을 호출할 때 운영체제가 제공하는 컨텍스트 값을 가리킵니다. 커널모드 호출인 경우 *ApcRoutine* 은 [**WORK\_QUEUE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff557304) 구조체를 가리키고 *ApcContext* 는 **WORK\_QUEUE\_ITEM** 구조체에 의해서 기술되는 워크 큐 아이템의 타입을 가리킵니다. 

이 섹션은 다음의 주제가 포함되어있습니다:

[**PreviousMode**](previousmode.md)

[Libraries and Headers](libraries-and-headers.md)

[What Does the Zw Prefix Mean?](what-does-the-zw-prefix-mean-.md)

[Specifying Access Rights](access-mask.md)

[NtXxx Routines](ntxxx-routines.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Nt%20and%20Zw%20Versions%20of%20the%20Native%20System%20Services%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


