package com.zhangkai.kasteme.kasteme.showactivities;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.zhangkai.kasteme.kasteme.R;
import com.zhangkai.kasteme.kasteme.customview.ScanView;

public class ScanActivity extends AppCompatActivity {

    private ScanView mScanView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scan);
        mScanView = new ScanView(this);
    }
}
