package com.zhangkai.kasteme.kasteme.showactivities;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.zhangkai.kasteme.kasteme.R;
import com.zhangkai.kasteme.kasteme.customview.KastemeView;

public class KaijunActivity extends AppCompatActivity{
KastemeView mView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_kaijun);
        mView = new KastemeView(this,null);
    }

}
