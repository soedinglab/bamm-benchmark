import os
import sys
import math
import string
import argparse
import scipy.stats
import warnings
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cycler
from collections import defaultdict
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

import warnings


## Resources from:
## https://matplotlib.org/users/customizing.html
## How to change color and plot styles? 
## https://matplotlib.org/users/dflt_style_changes.html
## mpl.rcParams[] = 

def wge_presentation():

    black = '#333333'
    linewidth = 2 
    ticksize = 8
    fontsize = 15 
    padding = 10
    labelpadding = 20
    fontfamily = 'system'
    dpi = 300
    #mcolors = wanwan_colors()

    warnings.filterwarnings('ignore')
    
    if fontfamily == 'system':
        mpl.rcParams['font.family'] = 'sans-serif'
        mpl.rcParams['font.sans-serif'] = 'DejaVu Sans'
        mpl.rcParams['mathtext.fontset'] = 'stixsans'

    elif fontfamily == 'latex':
        mpl.rcParams['text.latex.preamble'] = [
            r'\usepackage[sfdefault,scaled=.85, lining]{FiraSans}', 
            r'\usepackage[cmintegrals]{newtxsf}',
            r'\usepackage{microtype}', ]

        #mpl.rcParams['text.usetex'] = True
        
    elif fontfamily == 'latex-clearsans':
        mpl.rcParams['text.latex.preamble'] = [
            r'\usepackage[scaled=.86]{ClearSans}',
            r'\usepackage[libertine]{newtxmath}',
            r'\usepackage{microtype}',]

    # Size
    mpl.rcParams['figure.figsize'] = 8, 8
    mpl.rcParams['figure.dpi'] = dpi

    # Fonts
    mpl.rcParams['font.size'] = fontsize * 1.5
    mpl.rcParams['text.color'] = black

    mpl.rcParams['axes.titlesize'] = fontsize * 1.5
    mpl.rcParams['axes.labelsize'] = fontsize * 1.5
    mpl.rcParams['axes.labelweight'] = 'normal'
    mpl.rcParams['axes.labelcolor'] = black

    mpl.rcParams['xtick.labelsize'] = fontsize * 1.2
    mpl.rcParams['ytick.labelsize'] = fontsize * 1.2
    mpl.rcParams['legend.fontsize'] = fontsize * 1.2

    # Axes
    #mpl.rcParams['axes.titlepad'] = labelpadding
    mpl.rcParams['axes.labelpad'] = labelpadding
    mpl.rcParams['axes.edgecolor'] = black
    mpl.rcParams['axes.facecolor'] = 'white'
    mpl.rcParams['axes.linewidth'] = linewidth

    # Legend
    mpl.rcParams['legend.facecolor'] = 'inherit'
    mpl.rcParams['legend.edgecolor'] = black
    mpl.rcParams['legend.frameon'] = False
    mpl.rcParams['legend.numpoints'] = 1
    mpl.rcParams['legend.scatterpoints'] = 1
    mpl.rcParams['legend.markerscale'] = 1.0

    # Dimensions as fraction of fontsize
    mpl.rcParams['legend.borderpad'] = 0
    mpl.rcParams['legend.labelspacing'] = 0.2
    mpl.rcParams['legend.handlelength'] = 0.5
    mpl.rcParams['legend.handleheight'] = 0.9
    mpl.rcParams['legend.handletextpad'] = 0.5

    # Ticks
    mpl.rcParams['xtick.major.top'] = False
    mpl.rcParams['xtick.major.bottom'] = True
    mpl.rcParams['xtick.minor.top'] = False
    mpl.rcParams['xtick.minor.bottom'] = False
    mpl.rcParams['ytick.major.left'] = True
    mpl.rcParams['ytick.major.right'] = False
    mpl.rcParams['ytick.minor.left'] = False
    mpl.rcParams['ytick.minor.right'] = False

    mpl.rcParams['xtick.major.size'] = ticksize 
    mpl.rcParams['xtick.minor.size'] = 2 * ticksize / 3.0
    mpl.rcParams['ytick.major.size'] = ticksize
    mpl.rcParams['ytick.minor.size'] = 2 * ticksize / 3.0
    mpl.rcParams['xtick.major.pad'] = padding
    mpl.rcParams['xtick.minor.pad'] = padding
    mpl.rcParams['ytick.major.pad'] = padding
    mpl.rcParams['ytick.minor.pad'] = padding
    mpl.rcParams['xtick.major.width'] = linewidth
    mpl.rcParams['xtick.minor.width'] = linewidth
    mpl.rcParams['ytick.major.width'] = linewidth
    mpl.rcParams['ytick.minor.width'] = linewidth
    mpl.rcParams['xtick.color'] = black
    mpl.rcParams['ytick.color'] = black

    # for vline and hline
    mpl.rcParams['lines.linewidth'] = 3

    # Color cycle
    #mpl.rcParams['axes.prop_cycle'] = cycler('color', mcolors)

    # Histogram
    mpl.rcParams['hist.bins'] = 20

    # Patches
    # mpl.rcParams['patch.facecolor'] = mcolors[0] # doesn't have any effect, comes from prop_cycle
    mpl.rcParams['patch.edgecolor'] = black
    mpl.rcParams['patch.linewidth'] = linewidth / 2
    mpl.rcParams['patch.force_edgecolor'] = True

    # For scatter plot, show only left and bottom axes
    mpl.rcParams['axes.spines.left'] = True
    mpl.rcParams['axes.spines.bottom'] = True
    mpl.rcParams['axes.spines.top'] = True
    mpl.rcParams['axes.spines.right'] = True
    
    # Boxplot
    mpl.rcParams['boxplot.showcaps'] = True
    mpl.rcParams['boxplot.boxprops.linewidth'] = linewidth
    mpl.rcParams['boxplot.capprops.linewidth'] = 5
    
    return


def wanwan_colors(deeper = False):
    wanwan_colors_hex = [
        "#CC4300", # Grenadier Red
        "#E8743B", # Burnt Sienna
        "#F5AA85", # Tacao
        "#19A979", # Mountain Meadow
        "#367DC4", # Boston Blue
        "#93BFEB", # Perano Blue
        "#AEB89F", # Schist Gray
        "#616B77", # Shuttle Gray  
        ]
    wanwan_colors_hex_deeper = [
        "#7F2B01", # Grenadier Red
        "#813F1D", # Burnt Sienna
        "#94664F", # Tacao
        "#0F5E44", # Mountain Meadow
        "#234E79", # Boston Blue
        "#5F778E", # Perano Blue
        "#6D7364", # Schist Gray
        "#25282C", # Shuttle Gray  
        ]
    if deeper:
        return wanwan_colors_hex_deeper
    else:
        return wanwan_colors_hex


def wanwan_colors_add(deeper = False):
    wanwan_colors_nine = [
        "#CC4300", # Grenadier Red
        "#E8743B", # Burnt Sienna
        "#F5AA85", # Tacao
        "#FEBA05", # Yellow
        "#19A979", # Mountain Meadow
        "#367DC4", # Boston Blue
        "#93BFEB", # Perano Blue
        "#AEB89F", # Schist Gray
        "#616B77", # Shuttle Gray  
        ]
    wanwan_colors_nine_deeper = [
        "#7F2B01", # Grenadier Red
        "#813F1D", # Burnt Sienna
        "#94664F", # Tacao
        "#a87c06", # Yellow
        "#0F5E44", # Mountain Meadow
        "#234E79", # Boston Blue
        "#5F778E", # Perano Blue
        "#6D7364", # Schist Gray
        "#25282C", # Shuttle Gray  
        ]
    if deeper:
        return wanwan_colors_nine_deeper
    else:
        return wanwan_colors_nine

    
def wge_colors_3by5(deeper = False):
    wge_colors_3by5 = [

        "#d5dadc",
        "#9ea8ad",
        "#848f94",

        "#f8cc8c",
        "#f5b04d",
        "#f29b1d",

        "#a1dbb1",
        "#71c989",
        "#4cba6b",

        "#b2d4f5",
        "#74abe2",
        "#367dc4",
        
        "#f99494",
        "#f66364",
        "#f33334",
        
    ]
    
    wge_colors_3by5_deeper = [

        "#5f6365",
        "#5f6365",
        "#5f6365",

        "#7d5926",
        "#7d5926",
        "#7d5926",

        "#3a6746",
        "#3a6746",
        "#3a6746",

        "#3e5a76",
        "#3e5a76",
        "#3e5a76",
        
        "#953b3c",
        "#953b3c",
        "#953b3c",
        
    ]
    
    if deeper:
        return wge_colors_3by5_deeper
    else:
        return wge_colors_3by5


def wge_colors_2by5(deeper = False):
    wge_colors_2by5 = [

        "#d5dadc",
        "#848f94",

        "#f8cc8c",
        "#f29b1d",

        "#a1dbb1",
        "#4cba6b",

        "#b2d4f5",
        "#367dc4",

        "#f99494",
        "#f33334",
    ]
    wge_colors_2by5_deeper = [

        "#5f6365",
        "#5f6365",

        "#7d5926",
        "#7d5926",

        "#3a6746",
        "#3a6746",
        
        "#3e5a76",
        "#3e5a76",
        
        "#953b3c",
        "#953b3c",

    ]
    
    if deeper:
        return wge_colors_2by5_deeper
    else:
        return wge_colors_2by5

    
def wge_colors_4by3(deeper=False):
    
    wge_colors_4by3 = [
        
        "#f8cc8c",
        "#f5b04d",
        "#f29b1d",
        "#c67a0c",

        "#a1dbb1",
        "#71c989",
        "#4cba6b",
        "#358a4d",

        "#b2d4f5",
        "#74abe2",
        "#367dc4",
        "#1866b4", 
    ]

    wge_colors_4by3_deeper = [

        "#7d5926",
        "#7d5926",
        "#7d5926",
        "#7d5926",
        
        "#3a6746",
        "#3a6746",
        "#3a6746",
        "#3a6746",
        
        "#3e5a76",
        "#3e5a76",
        "#3e5a76",
        "#3e5a76",
                
    ]
    
    if deeper:
        return wge_colors_4by3_deeper
    else:    
        return wge_colors_4by3
                    
                    
# Utiliy function to create dictionary 
def multi_dict(K, type): 
    if K == 1: 
        return defaultdict(type) 
    else: 
        return defaultdict(lambda: multi_dict(K-1, type))     

    
# parser
def parser4plots(paras):
    
    # define meta table for storing all the data
    meta_table = multi_dict(3, float)
    
    keys = []
    for i, label in enumerate(paras.labels):
        # read in avrec score table
        stable = pd.read_csv(paras.scores[i], sep='\t', header=None,
                             names=['TF', 'num', 'd_avrec', 'd_occur', 'm_avrec', 'm_occur'])
        
        if paras.selected:
            if paras.pstyle == '5':
                for selected in paras.selected:
                    for j, TF in enumerate(stable['TF']):
                        if selected in TF and stable['d_avrec'][j] > paras.xcutoff:
                            meta_table[label][selected]['score'] += stable['d_avrec'][j]
                            meta_table[label][selected]['count'] += 1
            else:
                for selected in paras.selected:
                    for j, TF in enumerate(stable['TF']):
                        if selected in TF and stable['d_avrec'][j] > paras.xcutoff:
                            meta_table[label][TF]['avrec'] = stable['d_avrec'][j]  
        else:
            for j, TF in enumerate(stable['TF']):
                if stable['d_avrec'][j] > paras.xcutoff:
                    meta_table[label][TF]['avrec'] = stable['d_avrec'][j]

        # read in runtime table
        if paras.times:
            ttable = pd.read_csv(paras.times[i], sep='\t', header=None)
            for j, TF in enumerate(ttable[0]):
                meta_table[label][TF]['runtime'] = ttable[1][j]   

        for key, _ in meta_table[label].items():
            if key not in keys:
                keys.append(key)

    # for selected data sets
    if paras.selected and paras.pstyle == 'bar':
        for i, label in enumerate(paras.labels):
            for j, selected in enumerate(paras.selected):
                meta_table[label][selected]['avrec'] = meta_table[label][selected]['score'] / ( meta_table[label][selected]['count'] + 1e-6 )
        
    # remove the empty data sets
    removed_keys = []
    for i, label in enumerate(paras.labels):    
        for key in keys:
            if not meta_table[label][key]['avrec'] and key not in removed_keys:
                removed_keys.append(key)
    
    for i, label in enumerate(paras.labels):
        for key in removed_keys:
            del meta_table[label][key]
                
#    for i, label in enumerate(paras.labels):    
#        for j, (key, values) in enumerate(meta_table[label].items()):
#            if key == paras.dotname:
#                print(j)
 
    print('There are '+str(len(paras.labels))+' tools. Each has '+str(len(keys)-len(removed_keys))+'('+str(len(keys))+') data sets.')
    return meta_table


class para_parser(object):    
    def __init__(self, **args):
        self.__dict__.update(args)


def update_parser(paras_input): 
    
    default_paras = { 
        "figsize" : (8,8),
        "xlim"    : [],
        "ylim"    : [],
        "scores"  : [],
        "times"   : [],
        "labels"  : [],
        "pstyle"  : '',
        "title"   : '', 
        "lgdtitle": '', 
        "save_fn" : '',
        "xlabel"  : '', 
        "ylabel"  : '',
        "markers" : '',
        "xtick"   : (),
        "ytick"   : (),
        "yticklabel" : (),
        "xlog"    : False,
        "dotplot" : False,
        "legend"  : False,
        "noticks" : False,
        "legendout":False,
        "verbose" : False,
        "xcutoff" : 0,
        "ncluster": 0,
        "nameclus": [],
        "xlabel_box": '',
        "xlabel_scatter": '',
        "ylabel_scatter": '',
        "ytick_scatter" : (),
        "yticklabel_scatter" : (),  
        "ytick_dual": (),
        "xlim_dual": (4, 90000),
        "dotselected" : -1, # no dot is highlighted
        "dotname" : '',
        "selected": [],
        "diselect": [],
        "colors"  : wanwan_colors(),
        "median_colors": wanwan_colors(deeper=True),
        "hx_scatter" : 0.7,
        "hy_scatter" : 0.3,
        "xy_img"  : (0.45, 0.5),
        "hcolor"  : 'sienna',
        "lcolor"  : 'gray',
        "bcolor"  : 'gray',
        "scolor"  : "cornflowerblue",
        "legendcols" : False,
        "legend_nrow" : 0,
        "lspacing" : 0.40,
        "lhtpad"   : 0.3,
        "llmarign" : 0.,
        "lrmarign" : 1.,
        "ltmarign" : 1.,
    }
    
    for key, value in paras_input.items():
        default_paras[key] = value
        
    return default_paras


def wge_boxplot(meta_table, paras, axes):

    # plot label: 1
    
    data = []
    medians = []
    for i, label in enumerate(paras.labels):
        scores = []
        for TF, values in meta_table[label].items():
            scores.append(meta_table[label][TF]['avrec'])
        data.append(scores)
        medians.append(np.median(scores))
            
    df = pd.DataFrame(data, index=paras.labels)
    sns.boxplot(data=df.transpose(), 
               ax=axes,
               linewidth=2, 
               width = 0.7, 
               palette = paras.colors,
               boxprops={"zorder":10},
               whiskerprops={'linewidth': 2},
               medianprops={"zorder": 11, 'linewidth': 2})

    # Select each boxplot and color their edges individually.
    for i, artist in enumerate(axes.artists):
        mfacecolor=artist.get_facecolor()
        mlinecolor=paras.median_colors[i]
        artist.set_edgecolor(mlinecolor)
        # Each box has 6 associated Line2D objects (to make the whiskers, fliers, etc.)
        # Loop over them here, and use the same colour as above
        for j in range(i*6, i*6+6):
            line = axes.lines[j]
            line.set_color(mfacecolor)
            line.set_mfc(mfacecolor)
            line.set_mec(mfacecolor)
            # The 4th line is the median.
            if j==i*6+4:
                line.set_color(mlinecolor)
    
    # add hline due to max. median
    axes.axhline(y=max(medians), color=paras.lcolor, linestyle='dotted', alpha = 0.6, zorder = 20)

    # add dot plots
    if paras.dotplot:
        sns.swarmplot(x=paras.labels, y=data, data=df, color=".25", ax=axes)

    # label x ticks if there are clusters
    if paras.ncluster:
        ncolumn = int( len(paras.labels) / paras.ncluster)
        pad = float(ncolumn / 2)
        axes.set_xticks(np.arange(paras.ncluster)*ncolumn+pad-0.5)
        axes.set_xticklabels(paras.nameclus)
    else:
        axes.tick_params(bottom = False, top = False, left = True, right = False, 
                         labelleft = True, labelbottom = False)
    
    # highlight the example
    if paras.dotselected >= 0: 
        axes.text(0.98, 0.98, paras.dotname, 
                  ha='right', va='top', 
                  transform=axes.transAxes, 
                  weight='bold',
                  color=paras.hcolor)
        for i, label in enumerate(paras.labels):
            for j, (TF, values) in enumerate(meta_table[label].items()):
                if j == paras.dotselected:
                    print(TF)
                    axes.scatter(i, meta_table[label][TF]['avrec'], 
                                 color=paras.hcolor, 
                                 marker='o', edgecolor='white', 
                                 linewidth=2, 
                                 s = 80, 
                                 zorder = 30)
                    break
                
            
    if paras.noticks:
        if not paras.ncluster:
            axes.set_xticklabels([' ']*len(paras.labels))
    elif not paras.ncluster :
        axes.set_xticklabels(paras.labels, rotation=45, ha="center")
    
    if paras.xlabel_box:
        axes.set_xlabel(paras.xlabel_box)
    else:
        axes.set_xlabel('Motif finders')
        
    axes.set_ylabel('AvRec score')
    if paras.ytick:
        axes.set_yticks(paras.ytick)
        axes.set_yticklabels(paras.ytick)        
    else:
        axes.set_yticks((0.0,0.5,1.0))
        axes.set_yticklabels((0.0,0.5,1.0))
            
    return axes


def wge_cumuplot(meta_table, paras, axes):

    # plot label: 2

    n_bins = len(meta_table[paras.labels[0]])

    for i, label in enumerate(paras.labels):
        scores = []
        for TF, values in meta_table[label].items():
            scores.append(meta_table[label][TF]['avrec'])
            
        values, base = np.histogram(scores, bins=n_bins)
        cumulative = np.cumsum(values)
        axes.plot(n_bins-cumulative, base[:-1], c=paras.colors[i], label=label)

    if not paras.xtick:
        ulim = int( n_bins / 100 ) * 100
        mlim = int( ulim / 2 )
        axes.set_xticks((1, mlim, ulim))
    else: 
        axes.set_xticks(paras.xtick,paras.xtick)
        
    axes.set_xlabel('Data sets')
    axes.set_ylabel('AvRec score')
    
    if paras.ytick:
        axes.set_yticks(paras.ytick)
        axes.set_yticklabels(paras.ytick)        
    else:
        axes.set_ylim([-0.05,1.05])
        axes.set_yticks((0.0,0.5,1.0))
        axes.set_yticklabels((0.0,0.5,1.0))

    if paras.legend:
        leg = axes.legend(
            labels = paras.labels, 
              title  = paras.lgdtitle, 
              loc    = 'best', 
              handletextpad= paras.lhtpad,
              labelspacing = paras.lspacing,
             )
    return axes


def wge_dualplot(meta_table, paras, axes):
    
    # plot label: 3
    
    for i, label in enumerate(paras.labels):
        scores = []
        times = []
        for TF, values in meta_table[label].items():
            scores.append(meta_table[label][TF]['avrec'])
            times.append(meta_table[label][TF]['runtime'])
            
        # scatter plots:
        y_mean = np.mean(scores)
        x_mean = np.mean(times)
        x_std = np.std(times)
        
        axes.scatter(x_mean, y_mean, 
                     color=paras.colors[i], 
                     edgecolor=paras.median_colors[i],
                     linewidth = 2,
                     s=100, 
                     zorder=100, 
                     label = label)
        
        axes.errorbar(x_mean, y_mean, 
                      xerr=x_std, 
                      color=paras.colors[i], 
                      linewidth=2, 
                      alpha=1., 
                      capsize=6, 
                      zorder=50, 
                      capthick=2) 
    
    axes.set_xscale('log') 
    axes.set_xlabel("Runtime (seconds)")
    axes.set_xlim(paras.xlim_dual)
    axes.set_ylabel('AvRec score')
    
    if paras.ytick_dual:
        axes.set_yticks(paras.ytick_dual)
    else:
        axes.set_yticks((0.0,0.5,1.0))  
        
    leg = axes.legend(labels = paras.labels, 
                      title  = paras.lgdtitle, 
                      loc    = 'best', 
                      handletextpad= paras.lhtpad,
                      labelspacing = paras.lspacing,
                     )
        
    return axes  


def wge_scatterplot(meta_table, paras, axes):
    
    # plot label: 4

    scores = []
    ratios = []
    for i, (TF, values) in enumerate(meta_table[paras.diselect[0]].items()):
        score1 = meta_table[paras.diselect[0]][TF]['avrec']
        score2 = meta_table[paras.diselect[1]][TF]['avrec']
        scores.append(score1)
        ratios.append(score2/score1)

    avfc = np.median(ratios)
    axes.scatter(scores, ratios, marker='o', 
                 color=paras.scolor, alpha=0.3, edgecolor="mediumblue")
    
    axes.set_xlim([-0.05,1.05])

    axes.set_xticks((0.0,0.5,1.0))
        
    axes.set_yscale('log', basey=2)
    
    if paras.ytick_scatter:
        axes.set_ylim([paras.ytick_scatter[0]-0.15, paras.ytick_scatter[-1]+0.5])
        axes.set_yticks(paras.ytick_scatter)
        axes.set_yticklabels(paras.yticklabel_scatter)
    axes.axhline(y=1, color=paras.bcolor, alpha=0.6, linewidth=2)
    axes.axhline(y=avfc, color=paras.bcolor, alpha=0.6, linestyle='dotted', linewidth=2)
    axes.text(0.7, avfc+0.3, str(round((avfc-1)*100, 1))+'%', color=paras.bcolor)
            
    # highlight the example
    if paras.dotselected >= 0:
        axes.text(paras.hx_scatter, paras.hy_scatter, 
                  paras.dotname, 
                  ha='right', va='top', 
                  transform=axes.transAxes, 
                  color=paras.hcolor,
                  weight='bold',
                 )
        axes.scatter(scores[paras.dotselected], ratios[paras.dotselected], 
                     color=paras.hcolor, marker="o", edgecolor='white', 
                     linewidth=2, s = 100, zorder = 30)

    axes.set_xlabel(paras.xlabel_scatter)
    axes.set_ylabel(paras.ylabel_scatter)
    return axes


def statPlots(args):
    # active default settings
    wge_presentation()

    # update the parameters
    paras_input = update_parser(args)

    # read in all parameters 
    paras = para_parser(**paras_input)

    # read all the tables from input files
    meta_table = parser4plots(paras)

    # create the figure frame
    fig = plt.figure(figsize=paras.figsize)
    axes = plt.gca()
    
    if paras.pstyle == 'box':
        wge_boxplot(meta_table, paras, axes)
    elif paras.pstyle == 'cumu':
        wge_cumuplot(meta_table, paras, axes)
    elif paras.pstyle == 'dual':
        wge_dualplot(meta_table, paras, axes)
    elif paras.pstyle == 'scatter':
        wge_scatterplot(meta_table, paras, axes)
    elif paras.pstyle == 'bar':
        wge_barplot(meta_table, paras, axes)
    elif paras.pstyle == 'violin':
        wge_violinplot(meta_table, paras, axes)
    else: 
        print("ERROR: pstyle is not defined!")
        
    plt.tick_params(length=6, direction='out')
    
    if paras.xlog:
        axes.set_xscale('log') 
    if paras.title:
        axes.set_title(paras.title+'\n')
    if paras.xlabel:
        axes.set_xlabel(paras.xlabel)
    if paras.ylabel:
        axes.set_ylabel(paras.ylabel)
    #if paras.xtick and paras.pstyple != "box":
    #    plt.xticks(paras.xtick,paras.xtick) 
    if paras.ytick:
        plt.yticks(paras.ytick,paras.ytick)  
        
    if paras.legendout:
        #plt.setp(axes.get_xticklabels(), visible=False)
        legend=plt.legend(labels = paras.labels, 
                          title  = paras.lgdtitle, 
                          loc    = 'center left', 
                          bbox_to_anchor=(1, 0.5),
                          handletextpad= paras.lhtpad,
                          labelspacing = paras.lspacing,
                         )        
    elif paras.legend:
    #elif paras.showlegend:
        legend=plt.legend(labels = paras.labels, 
                          title  = paras.lgdtitle, 
                          loc    = 'best', 
                          handletextpad= paras.lhtpad,
                          labelspacing = paras.lspacing,
                         )
        if paras.legendcols:
            lnrow = paras.legend_nrow
            mhandles, mlabels = axes.get_legend_handles_labels()
            legend1 = axes.legend(handles = mhandles[:lnrow], 
                                  labels = mlabels[:lnrow],
                                  loc = 'upper left', 
                                  bbox_to_anchor = (paras.llmarign, paras.ltmarign), 
                                  handletextpad= paras.lhtpad,
                                  labelspacing = paras.lspacing,
                                  frameon = False)
            legend2 = axes.legend(handles = mhandles[lnrow:], 
                                  labels = mlabels[lnrow:],
                                  loc = 'upper right', 
                                  bbox_to_anchor = (paras.lrmarign, paras.ltmarign), 
                                  handletextpad= paras.lhtpad,
                                  labelspacing = paras.lspacing,
                                  frameon = False)
            plt.gca().add_artist(legend1)
            
    #if paras.noticks:
    #    plt.setp(axes.get_xticklabels(), visible=False)
        
    
    if paras.xlim:
        axes.set_xlim(paras.xlim[0], paras.xlim[1])
    if paras.ylim:
        axes.set_ylim(paras.ylim[0], paras.ylim[1])
    
       
    # save plot
    plt.tight_layout()
    if paras.save_fn:
        fig.savefig(paras.save_fn, bbox_inches='tight')
    plt.show()
    
    return


def benchPlots(args):
    # active default settings
    wge_presentation()

    # update the parameters
    paras_input = update_parser(args)

    # read in all parameters 
    paras = para_parser(**paras_input)

    # read all the tables from input files
    meta_table = parser4plots(paras)
    
    # plot label: bench_cv
    fig, axes = plt.subplots(2, 3, figsize=(20,13))
        
    #fig.suptitle(paras.title)
    #df = pd.DataFrame(meta_table)
    
    # Figure A
    axes[0, 0].axis('off')
    if paras.figpath1:
        img1 = mpimg.imread(paras.figpath1)
        fig1 = AnnotationBbox(OffsetImage(img1, zoom=0.06), paras.xy_img, frameon=False)
        axes[0, 0].add_artist(fig1)
        
    # Figure B
    axes[0, 1].axis('off')
    if paras.figpath2:
        img2 = mpimg.imread(paras.figpath2)
        fig2 = AnnotationBbox(OffsetImage(img2, zoom=0.06), paras.xy_img, frameon=False)
        axes[0, 1].add_artist(fig2)
    
    # Figure C
    wge_scatterplot(meta_table, paras, axes=axes[0, 2])
    
    # Figure D
    wge_boxplot(meta_table, paras, axes=axes[1, 0])
    
    # Figure E
    wge_cumuplot(meta_table, paras, axes=axes[1, 1])
   
    # Figure F
    wge_dualplot(meta_table, paras, axes=axes[1, 2])
    
    # annotate subfigures
    for n, ax in enumerate(fig.axes):
        ax.text(-0.1, 1.1, 
                '('+string.ascii_uppercase[n]+')',
                transform=ax.transAxes, 
                size=30,
                weight='bold')
        
    # control the distance between two rows
    plt.subplots_adjust(hspace=1.5)
    plt.tight_layout()
    plt.show()
    
    # save plot into .pdf file 
    if paras.save_fn:
        fig.savefig(paras.save_fn, bbox_inches='tight')

    return


def combine3plots(args_cl, args_cs, args_sc, save_fn=''):

    # active default settings
    wge_presentation()

    # update the parameters
    paras_input_cl = update_parser(args_cl)
    paras_input_sc = update_parser(args_sc)
    paras_input_cs = update_parser(args_cs)

    # read in all parameters 
    paras_cl = para_parser(**paras_input_cl)
    paras_sc = para_parser(**paras_input_sc)
    paras_cs = para_parser(**paras_input_cs)

    # read all the tables from input files
    meta_table_cl = parser4plots(paras_cl)
    meta_table_sc = parser4plots(paras_sc)
    meta_table_cs = parser4plots(paras_cs)

    # plot label: bench_cv
    fig, axes = plt.subplots(2, 3, figsize=(20,13))

    # Figure A-C
    wge_boxplot(meta_table_cl, paras_cl, axes=axes[0, 0])
    wge_boxplot(meta_table_cs, paras_cs, axes=axes[0, 1])
    wge_boxplot(meta_table_sc, paras_sc, axes=axes[0, 2])

    # Figure D-E
    wge_cumuplot(meta_table_cl, paras_cl, axes=axes[1, 0])
    wge_cumuplot(meta_table_cs, paras_cs, axes=axes[1, 1])
    wge_cumuplot(meta_table_sc, paras_sc, axes=axes[1, 2])


    # annotate subfigures
    for n, ax in enumerate(fig.axes[:3]):
        ax.text(-0.1, 1.1, 
                '('+string.ascii_uppercase[n]+')',
                transform=ax.transAxes, 
                size=30,
                weight='bold')

    # control the distance between two rows
    plt.subplots_adjust(hspace=1.5)
    plt.tight_layout()
    plt.show()

    # save plot into .pdf file 
    if save_fn:
        fig.savefig(save_fn, bbox_inches='tight')
    return


def flankPlots(args_flank_encode, args_flank_selex, save_fn=''):
    # active default settings
    wge_presentation()

    # update the parameters
    paras_input_encodef = update_parser(args_flank_encode)
    paras_input_selexf = update_parser(args_flank_selex)

    # read in all parameters 
    paras_encodef = para_parser(**paras_input_encodef)
    paras_selexf = para_parser(**paras_input_selexf)

    # read all the tables from input files
    meta_table_encodef = parser4plots(paras_encodef)
    meta_table_selexf = parser4plots(paras_selexf)

    # plot label: bench_cv
    fig, axes = plt.subplots(2, 2, figsize=(12,12))

    # Figure A
    wge_boxplot(meta_table_encodef, paras_encodef, axes=axes[0, 0])

    # Figure B
    wge_scatterplot(meta_table_encodef, paras_encodef, axes=axes[0, 1])

    # Figure C
    wge_boxplot(meta_table_selexf, paras_selexf, axes=axes[1, 0])

    # Figure D
    wge_scatterplot(meta_table_selexf, paras_selexf, axes=axes[1, 1])


    # annotate subfigures
    for n, ax in enumerate(fig.axes):
        ax.text(-0.1, 1.1, 
                '('+string.ascii_uppercase[n]+')',
                transform=ax.transAxes, 
                size=30,
                weight='bold')

    # control the distance between two rows
    plt.subplots_adjust(hspace=1.5)
    plt.tight_layout()
    plt.show()

    # save plot into .pdf file 
    if save_fn:
        fig.savefig(save_fn, bbox_inches='tight')
    return
    
    
