### 史诗级user story ###
1. 作为一名股民, 我希望能有一个选股神器, 以便我能选出心仪的股票.

    - #### 基础搜索指标相关user story ####
        + 1.1 作为一名新手炒股用户, 我希望系统提供一些股票基本指标, 以便我能搜索到一些标准的信息
            - 1.1.1 作为一名用户, 我希望系统提供一些股票基本指标, 以便我能搜索到一些标准的信息. (聂禾) 
                + 基本指标：
                    - 总市值(亿)    
                    - 流通市值(亿)   
                    - 动态市盈率(倍)  
                    - 静态市盈率(倍)
                    - 每股收益  
                    - 每股净资产 
                    - 净资产收益率(%) 
                    - 净利润(万)
                    - 股息率(%)    
                    - 市净率(倍)
        
                + **没有对应代码**

    - #### 范围精确查询user story  ####
        + 1.2作为一名资深炒股用户, 我希望系统能够根据我输入的条件来进行搜索, 以便我能够找出最心仪的股票.
            - 1.2.1 作为一名用户, 我希望系统在我勾选了某个指标之后才显示具体的输入范围, 以便我只对某一些指标进行筛选.
                + 1.2.1.1 作为一名资深用户, 我希望系统能以滚动条的形式让我输入筛选条件范围值, 以便我直观操作. (作恒) 
                    + 涉及:
                        - view/qrange_slider.py
                        - view/qdistribution_slider.py
                        - controller/stock_ctrl.py

            - 1.2.2作为一名资深用户, 我希望系统能够把筛选指标标准尽量具体, 以便我能更加准确地找出目标股票. (作恒)
                + 筛选标准应该包含：
                    - 最小值   
                    - 条件范围/股票分布 
                    - 最大值   
                    - 日期设置

                + 涉及:
                    - view/qdistribution_slider.py
                    - view/qscreener_item.py
                    - view/qscreener.py


    - #### 收藏搜索条件相关user story ####
        - 1.2.4 作为一名资深用户, 我希望系统提供按钮用于保存搜索条件, 以便我下次迅速查询, 不用再次输入.
            + 1.2.4.1作为一个资深用户, 我希望系统能提供一个下拉列表来让我选择以往保存的搜索条件, 以便我直接使用以前的搜索条件.  (作恒)
                - 涉及:
                    - view/fav_wrapper.py
                    - view/fav_item.py
                    - controller/fav_ctrl.py
                    - view/qhover_button.py
                    - dao/fav_dao.py
                    - view/new_fav_dlg.py

            + 1.2.4.2 作为一个资深用户, 我希望系统在我选择了某个收藏搜索条件时能动态刷新各种标准的范围值, 以便我浏览该搜索条件的具体信息.  (作恒)
                - 涉及:
                    - controller/fav_ctrl.py
                    - controller/wrapper_group_ctrl.py
                    - controller/main_ctrl.py
                    - controller/screener_group_ctrl.py
                    - controller/screener_ctrl.py

            + 1.2.4.3作为一个资深用户, 我希望系统能在我更改了收藏的搜索条件的时候提供保存和新增收藏的按钮, 以便我修改收藏搜索条件.  (长荣)
                - 涉及:
                    - controller/fav_ctrl.py
                    - controller/wrapper_group_ctrl.py
                    - controller/main_ctrl.py
                    - controller/screener_group_ctrl.py
                    - controller/screener_ctrl.py
            + 1.2.4.4作为一个资深用户, 我希望系统提供按钮用于删除收藏的搜索条件, 以便我维护自己的搜索条件.  (长荣)
                - 涉及:
                    - view/fav_item.py
                    - controller/fav_ctrl.py
                    - view/qwarning_message_box.py
                    - dao/fav_dao.py

    - #### 更新数据库user story ####
        + 1.3作为一名用户, 我希望系统能够提供更新功能, 以便我能看到最新的股票信息. (叶晨) 
            - 涉及:
                - view/refresh_widget.py
                - service/wencai_refresh_thread.py
                - service/xueqiu_refresh_thread.py
            

    - #### 重置搜索条件user story ####
        + 1.4 作为一名用户, 我希望系统提供重置按钮, 以便我快速查询其他目标股票. (叶晨) 
            - 涉及:
                - view/qscreener.py
                - controller/screener_ctrl.py
                - controller/screener_group_ctrl.py
                - controller/main_ctrl.py
                - controller/wrapper_group_ctrl.py
                - controller/wrapper_ctrl.py
                - view/qcondition_wrapper.py
                - view/qid_checkbox.py

    - #### 搜索结果相关user story ####
        + 1.5作为一个用户, 我希望系统能提供给我友好的界面, 以便我能进行快速方便进行股票信息查询.
            - 1.5.1作为一名用户, 我希望系统能够在查询结果列表显示出每种股票的具体信息, 以便我浏览和进一步筛选. (聂禾) 
                + 列表应该包含的具体信息有：
                    - 当前价   
                    - 本日涨跌幅(%)
                    - 动态市盈率(倍)  
                    - 净资产收益率(%) 
                    - 市净率(倍)    
                    - 每股收益
                    - 净利润(万)    
                    - 流通市值(亿)   
                    - 总市值(亿)    
                    - 静态市盈率(倍)  
                    - 股息率(%)    
                    - 每股净资产
                + 涉及:   
                    - controller/stock_ctrl.py
                    - controller/title_ctrl.py
                    - dao/title_dao.py
                    - model/wencai_stock.py
                    - view/qresult_dialog.py

    - #### 数据库相关user story####
        + 1.6作为开发者, 我希望系统能够获取网上公开的股票信息, 以便保存数据和更新数据.   
            - 1.6.1作为开发者, 我希望系统可以存储从网上获取的所有股票信息, 以便筛选等后续处理. (叶晨) 
                + 涉及:
                    - dao/wencai_dao.py
                    - dao/sqlite_stock_dao.py
                    - service/wencai_spider.py
                    - service/xueqiu_spider.py
                    - controller/stock_ctrl.py
                    - dao/wencai_dao.py

    - #### 切换数据来源相关user story
        + 1.7 作为一个用户，希望能够获取不止一个的股票信息网页的搜索数据，以便应对某个网页信息失灵的情况。 (叶晨)
            - 涉及:
                - view/qindex_list.py
                - view/index_list_item.py
                - controller/index_list_ctrl.py
                - view/qicon_widget.py
        + 1.8 作为用户, 我希望UI上能够提供按钮给我选择股票来源，以便我可以选择确切的股票信息搜索数据来源。  (作恒) 
            - 涉及: 
                - 同上
        + 1.9 作为用户, 我希望对不同来源的股票查询指标进行收藏, 查询出来的解决具有特色。
            1.9.1 作为用户, 我希望系统UI能够提供搜藏按钮, 能让我对不同来源的股票指标进行收藏。(作恒)
            1.9.2 作为用户, 我希望系统UI能够提供修改按钮, 能让我对不同来源的股票收藏指标进行修改。（长荣）
            1.9.3 作为用户, 我希望系统UI能够提供删除按钮, 能让我对不同来源的股票收藏指标进行删除。（聂禾）
            - 涉及:
                (你TM这三个backlog就是废话, 给我写清楚点)
