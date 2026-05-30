from market import get_market_data
from ai_summary import create_summary
from kakao import send_message

def main():

    market_data = get_market_data()

    summary = create_summary(
        market_data
    )

    print(summary)

    send_message(summary)

if __name__ == "__main__":
    main()