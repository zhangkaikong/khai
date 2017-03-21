package com.zhangkai.kasteme.kasteme;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class KaijunActivity extends AppCompatActivity {
KastemeView mView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_kaijun);
        mView = new KastemeView(this,null);
    }
}
