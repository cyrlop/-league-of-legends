# -*- coding: utf-8 -*-

def label_bars(ax, perc=False):
    for p in ax.patches:
        b = p.get_bbox()
        val = "{:.3}{}".format(b.y1, "%" if perc else "")        
        ax.annotate(val, ((b.x0 + b.x1)/2 - 0.075 , b.y1+1))
    
    return ax