# import plotly
# import plotly.graph_objs as go

def building_graphics():
    a1 = [i + 10 for i in h_vk_overWother]
    a1 = [1500-i for i in a1]
    a = [1500-i for i in h_vk]

    b = [round(((len(a) - i)/len(a))*(bmax-bmin) + 10, 1) for i in range(len(a))]
    print(len(b), len(a), len(a1))
    x = np.arange(500) / 500 + np.arange(500) / 500 + np.arange(500) / 500 + np.arange(500) / 500 + np.arange(500) / 500
    y = (np.arange(
        len(a) + len(a1)) * 0)  # + (np.arange(500)*0) + 1 + (np.arange(500)*0) + 2 + (np.arange(500)*0) + 3 +
    d = np.random.randint(low=1, high=100, size=500) / 10
    e = np.random.randint(low=10, high=100, size=500) / 10

    fig1 = go.Scatter3d(x=z2,
                        y=a2,
                        z=b2,
                        marker=dict(opacity=0.9,
                                    reversescale=True,
                                    colorscale='Blues',
                                    size=5),
                        line=dict(width=0.02),
                        mode='lines+markers')

    # Make Plot.ly Layout
    mylayout = go.Layout(scene=dict(xaxis=dict(title="x"),
                                    yaxis=dict(title="y"),
                                    zaxis=dict(title="z")), )

    # Plot and save html
    plotly.offline.plot({"data": [fig1],
                         "layout": mylayout},
                        auto_open=True,
                        filename=("3DPlot.html"))