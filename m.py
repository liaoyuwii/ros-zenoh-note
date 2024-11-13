import time
import zenoh

def main():
    session = zenoh.open(zenoh.Config())

    # 訂閱溫度數據 (接收字串)
    def listener(sample):
        try:
            # 將 ZBytes 物件轉換為 bytes 並解碼為 UTF-8 字串
            payload_bytes = bytes(sample.payload)
            temperature_str = payload_bytes.decode('utf-8')
            print(f"Received temperature: {temperature_str}")
        except (UnicodeDecodeError, TypeError) as e:
            print(f"Error: Unable to decode payload as UTF-8 string - {e}")

    subscriber = session.declare_subscriber('home/kitchen/sensor/temp', listener)

    try:
        # 保持訂閱狀態
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Subscription stopped by user.")
    finally:
        subscriber.undeclare()
        session.close()

if __name__ == "__main__":
    main()
