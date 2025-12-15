import matplotlib.pyplot as plt
import uuid

def create_chart(df, x, y, chart_type="bar"):
    filename = f"chart_{uuid.uuid4().hex}.png"

    if chart_type == "bar":
        df.plot(kind="bar", x=x, y=y)
    elif chart_type == "line":
        df.plot(kind="line", x=x, y=y)
    else:
        df.plot(kind="bar", x=x, y=y)

    plt.tight_layout()
    plt.savefig(f"charts/{filename}")
    plt.close()

    return filename
