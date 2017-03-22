package com.zhangkai.kasteme.kasteme.showactivities;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.zhangkai.kasteme.kasteme.R;
import com.zhangkai.kasteme.kasteme.customview.AnimatorView;

public class AnimatorActivity extends AppCompatActivity {
private AnimatorView mAnimatorView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_animator);
        mAnimatorView = new AnimatorView(this);
    }
}
