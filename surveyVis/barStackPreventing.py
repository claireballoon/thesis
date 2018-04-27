import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def numResponses(df, responseNo):
    return len(df.loc[df['preventingSH']==responseNo,['preventingSH']]);

def barStackPrev(face,yout,insta,twit,snap,redd,tumbl,other):
    objects = ['Facebook','YouTube','Instagram','Twitter','Snapchat','Reddit'];
    #objects = ['Facebook','YouTube','Instagram','Twitter','Snapchat','Reddit','Tumblr','Other'];
    #objects = ('Other','Tumblr','Reddit','Snapchat','Twitter','Instagram','YouTube','Facebook');
    #n_groups = len(objects);
    #index = np.arange(len(objects));
    #bar_width = 0.18;
    #opacity=0.8;
    ind = [x for x, _ in enumerate(objects)];

    #notadequate=np.array([numResponses(face,'1'), numResponses(yout,'1'),numResponses(insta,'1'),numResponses(twit,'1'),numResponses(snap,'1'),numResponses(redd,'1'),numResponses(tumbl,'1'),numResponses(other,'1')],dtype=float);
    #some=np.array([numResponses(face,'2'), numResponses(yout,'2'),numResponses(insta,'2'),numResponses(twit,'2'),numResponses(snap,'2'),numResponses(redd,'2'),numResponses(tumbl,'2'),numResponses(other,'2')],dtype=float);
    #adequate=np.array([numResponses(face,'3'), numResponses(yout,'3'),numResponses(insta,'3'),numResponses(twit,'3'),numResponses(snap,'3'),numResponses(redd,'3'),numResponses(tumbl,'3'),numResponses(other,'3')],dtype=float);
    #idk=np.array([numResponses(face,'4'), numResponses(yout,'4'),numResponses(insta,'4'),numResponses(twit,'4'),numResponses(snap,'4'),numResponses(redd,'4'),numResponses(tumbl,'4'),numResponses(other,'4')],dtype=float);

    notadequate=np.array([numResponses(face,'1'), numResponses(yout,'1'),numResponses(insta,'1'),numResponses(twit,'1'),numResponses(snap,'1'),numResponses(redd,'1')],dtype=float);
    some=np.array([numResponses(face,'2'), numResponses(yout,'2'),numResponses(insta,'2'),numResponses(twit,'2'),numResponses(snap,'2'),numResponses(redd,'2')],dtype=float);
    adequate=np.array([numResponses(face,'3'), numResponses(yout,'3'),numResponses(insta,'3'),numResponses(twit,'3'),numResponses(snap,'3'),numResponses(redd,'3')],dtype=float);
    idk=np.array([numResponses(face,'4'), numResponses(yout,'4'),numResponses(insta,'4'),numResponses(twit,'4'),numResponses(snap,'4'),numResponses(redd,'4')],dtype=float);

    total = adequate+some+notadequate+idk;
    proportion_nota = np.true_divide(notadequate,total, out=np.zeros_like(notadequate), where=total!=0)*100;
    proportion_some = np.true_divide(some,total, out=np.zeros_like(some), where=total!=0)*100;
    proportion_adeq = np.true_divide(adequate,total, out=np.zeros_like(adequate), where=total!=0)*100;
    proportion_idk = np.true_divide(idk,total, out=np.zeros_like(idk), where=total!=0)*100;

    stat1=plt.bar(ind, proportion_nota, width=0.8, label='Not Adequate',color='#450a5cff',bottom=proportion_some+proportion_adeq+proportion_idk);
    stat2=plt.bar(ind, proportion_some, width=0.8, label='Somewhat',color='#2d6e8eff',bottom=proportion_adeq+proportion_idk);
    stat3=plt.bar(ind, proportion_adeq, width=0.8, label='Adequate',color='#49be6eff',bottom=proportion_idk);
    stat4=plt.bar(ind, proportion_idk, width=0.8, label='I don\'t know',color='#e1e329ff');

    plt.xticks(ind, objects)
    plt.ylabel("Percentage of Responses")
    plt.xlabel("Social Media Platforms")
    #plt.legend(loc="upper right")
    plt.title('Ability to Prevent Sexual Harassment')
    plt.ylim=1.0;
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    #plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",mode='expand',ncol=4);
    #plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
    plt.legend(loc='lower center', ncol=2);
    #first_legend = plt.legend(handles=[stat1,stat2], loc=3);
    #second_legend = plt.legend(handles=[stat3,stat4], loc=4);

    #plt.tight_layout();
    #fig = plt.figure(1);
    plt.savefig("stackPreventing.pdf", bbox_inches="tight");
    plt.savefig("stackPreventing.png", bbox_inches="tight");
    plt.show();
